import pytest


    
@pytest.fixture(scope="package",autouse=True)
def thisis_packageFixer2():
    print("this is before package2");
    yield
    print("this is after package2")