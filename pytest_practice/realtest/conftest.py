#这个文件必须要叫这个名字
import pytest

@pytest.fixture(scope="function")
def login():
    print('logging...............')


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("关闭浏览器")

