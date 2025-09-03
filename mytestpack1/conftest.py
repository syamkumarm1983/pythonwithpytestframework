import pytest

@pytest.fixture(scope="package",autouse=True)
def thisis_packageFixer():
    print("this is before package");
    yield
    print("this is after package")
    
