import copy
import os
import json


def read_cheese_preferences():
    full_path = os.path.expanduser("~/cheese.json")
    with open(full_path, "r") as f:
        prefs = json.load(f)
    return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser("~/cheese.json")
    print("full_path = " , full_path)
    with open(full_path, "w") as f:
        json.dump(prefs, f, indent=4)


def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)


_default_prefs = {
    "slicing": ["manchego", "sharp cheddar"],
    "spreadable": ["Saint Andre", "camembert", "bucheron", "goat", "humbolt fog", "cambozola"],
    "salads": ["crumbled feta"]
}


def test_def_prefs_full(tmpdir, monkeypatch):
    #monkeypatch.setenv("HOME", tmpdir.mkdir("home"))
    fake_home_dir = tmpdir.mkdir("home")
    monkeypatch.setattr(os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir))))
    write_default_cheese_preferences()
    expected = _default_prefs
    actual = read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    # write the file once
    fake_home_dir = tmpdir.mkdir("home")
    monkeypatch.setattr(os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir))))
    write_default_cheese_preferences()
    defaults_before = copy.deepcopy(_default_prefs)

    # change the defaults
    monkeypatch.setitem(_default_prefs, "slicing", ["provolone"])
    monkeypatch.setitem(_default_prefs, "spreadable", ["brie"])
    monkeypatch.setitem(_default_prefs, "salads", ["pepper jack"])
    defaults_modified = _default_prefs

    # write it again with modified defaults
    write_default_cheese_preferences()

    # read, and check
    actual = read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before