import pytest


@pytest.fixture(scope='session')
def ff():
    print('this is a fixture,but be used by f')

@pytest.fixture(autouse=True,scope='session')
def f(ff):
    print("before executing the use case")
    yield
    print("after executing the use case")