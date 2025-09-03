import pytest


    
@pytest.fixture(scope="package",autouse=True)
def thisis_packageFixer1():
    print("this is before package1");
    yield
    print("this is after package1")