import pytest, time


def test_tmpdir(tmpdir):
    # 创建一个文件
    a_file = tmpdir.join("something.txt")
    print(a_file)
    # 创建一个文件夹 anything
    a_sub_dir = tmpdir.mkdir("anything")
    # 在创建的文件夹中再创建一个文件
    another_file = a_sub_dir.join("something_sele.txt")
    # 在文件中写入数据
    a_file.write("contents mat settle during shipping")

    another_file.write("something different")
    # 读取并比对
    assert a_file.read() == "contents mat settle during shipping"
    assert another_file.read() == "something different"

def test_tmpdir_factory(tmpdir_factory):
    # 相当于创建一个文件夹，相当于比 tmpdir要多做这一步操作。目录mydir
    a_dir = tmpdir_factory.mktemp("mydir")

    base_temp = tmpdir_factory.getbasetemp()
    print("base:", base_temp)  # test_scope.py base: C:\Users\admin\AppData\Local\Temp\pytest-of-admin\pytest-11

    a_file = a_dir.join("something.txt")
    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join("something_else.txt")

    a_file.write("contents may settle during shipping")
    another_file.write("something different")

    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"