import pytest

@pytest.fixture(scope="class",autouse=True)
def this_is_class_scope():
    print("before class")
    yield
    print("after class")

@pytest.fixture(scope="function")
def this_is_function_scope():
    print("before function")
    yield
    print("after function")

@pytest.fixture(scope="module")
def this_is_module_scope():
    print("before module")
    yield
    print("after module")

def test_class4(this_is_function_scope): 
        print("this is class test4")     
def test_class5(this_is_function_scope): 
        print("this is class test5")  
def test_class6(this_is_module_scope): 
        print("this is class test6")  
def test_class7(this_is_module_scope): 
        print("this is class test7")  
def test_class8(this_is_module_scope): 
        print("this is class test8")  

class Testsampleclss:
    def test_class1(self):
        print("this is class test1")
    def test_class2(self):
        print("this is class test2")       
    def test_class3(self):
        print("this is class test3")   
                                       