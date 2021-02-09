def test_capsys_disabled(capsys):
    with capsys.disabled():
        print("\nalways print this")
    print("normal print, usually captured")
    out, err = capsys.readouterr()
    assert out == "normal print, usually captured\n"

def test_capsys_disabled2(capsys):
    print("\nalways print this")
    print("normal print, usually captured")
    out, err = capsys.readouterr()
    assert out == "\nalways print this\nnormal print, usually captured\n"