import pytest

class Testcls1():
    def test_one(self):
        print("this is one")
        assert 'a' in 'abc'
        pytest.assume('b' not in 'abc')  #assume 即使断言失败也能继续执行
        assert 'c' in 'abc'
        print('acbd')

    def test_two(self):
        print("this is one")
        assert 'a' in 'abc'

@pytest.mark.filter
class Testcls2():
    def test_two2(self):
        print("this is one")
        assert 'a' not in 'abc'

    def test_need1(self,login,open):
        print('第一个需要登陆')

    def test_need2(self,login,open):
        print('第二个不需要登陆')

#。。。。。。。。。。。。。。。。。。。 接受测试数据。。。。。。。。。。。。。。。。。。。。。。。。
@pytest.mark.parametrize("input,output",[(1,2),(3,3),(5,6)])
def test_equl(input,output):
     pytest.assume(input == output)

if __name__ == '__main__':
    # pytest.main(['-v','-s','test_demo.py::Testcls1'])
    pytest.main(['-v','-s','test_demo.py','-m','filter'])
