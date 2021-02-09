# 方式一
import allure

@allure.feature("description 测试")
class TestDescription():
    @allure.description("""
    这是一个@allure.description装饰器
    没有特别的用处
    """)
    def test_description_from_decorator(self):
        assert 42 == int(6 * 7)


    # 方式二
    def test_unicode_in_docstring_description(self):
        """
        当然，在方法声明的下一行这样子写，也算一种添加description的方式哦
        """
        assert 42 == int(6 * 7)


    # 方式三
    @allure.description_html("""
    <h1>Test with some complicated html description</h1>
    <table style="width:100%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
      </tr>
      <tr align="center">
        <td>William</td>
        <td>Smith</td>
    </table>
    """)
    def test_html_description(self):
        assert True
