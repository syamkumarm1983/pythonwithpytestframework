import pytest

@pytest.fixture(scope="session",autouse=True)
def thisis_before_suite():
    print("this is before suite");
    yield
    print("this is after suite")
    
