import allure

@allure.feature('epic 测试')
class TestEpic():

    def test_without_any_annotations_that_wont_be_executed(self):
        pass


    @allure.epic('epic_1')
    def test_with_epic_1(self):
        pass


    @allure.story('story_1')
    def test_with_story_1(self):
        pass


    @allure.story('story_2')
    def test_with_story_2(self):
        pass


    @allure.feature('feature_2')
    @allure.story('story_2')
    def test_with_story_2_and_feature_2(self):
        pass
