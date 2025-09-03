import pytest

@pytest.fixture(scope="session",autouse=True)
def thisis_before_suite():
    print("this is before suite");
    yield
    print("this is after suite")
    
@pytest.fixture(scope="package",autouse=True)
def thisis_packageFixer():
    print("this is before package");
    yield
    print("this is after package")