import pytest

@pytest.mark.web
def test_web(driver):
    print(">>> 测试函数已进入")
    driver.get("https://www.baidu.com")
    print(">>> 页面已加载")
    print(driver.url)