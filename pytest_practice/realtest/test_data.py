import pytest
import yaml
import allure


class Testyaml():
    @allure.link(url="https://www.baidu.com", name="link")
    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./data.yaml")))
    def test_prac1(self,a,b):
        print(a+b)
        print(yaml.safe_load(open("./data.yaml")))

    def test_prac2(self):
        pytest.assume('a' in 'abc')
