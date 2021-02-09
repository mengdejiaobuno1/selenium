import allure

@allure.feature("severity 测试")
def test_with_no_severity_label():
    pass

@allure.feature("severity 测试")
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.feature("severity 测试")
@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.feature("severity 测试")
@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        """ 测试类优先级 normal；看看测试用例是否会自动继承优先级 """
        print()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        """
        测试类优先级 normal
        测试用例优先级 critical
        """
        pass

@allure.feature("severity 测试")
@allure.severity("normal")
def test_case_1():
    """ normal 级别测试用例 """
    print("test case normal")

@allure.feature("severity 测试")
@allure.severity("critical")
def test_case_2():
    """ critical 级别测试用例 """
    print("test case critical")

@allure.feature("severity 测试")
@allure.severity("blocker")
def test_case_3():
    """ blocker 级别测试用例 """
    print("test case blocker")

@allure.feature("severity 测试")
@allure.severity("minor")
def test_case_4():
    """ minor 级别测试用例 """
    print("test case minor")

@allure.feature("severity 测试")
def test_case_5():
    """ 没标记 severity 的用例默认为 normal"""
    print("test case default")