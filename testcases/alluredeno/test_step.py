import allure

@allure.feature("step 测试")
class TestStep():

    @allure.step("第一步")
    def passing_step(self):
        pass


    @allure.step("第二步")
    def step_with_nested_steps(self):
        self.nested_step()


    @allure.step("第三步")
    def nested_step(self):
        self.nested_step_with_arguments(1, 'abc')


    @allure.step("第四步{0}，{arg2}")
    def nested_step_with_arguments(self, arg1, arg2):
        pass


    @allure.step("第五步")
    def test_with_nested_steps(self):
        self.passing_step()
        self.step_with_nested_steps()