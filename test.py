from hello import hello_world
from hello import hello_there
from hello import add
from hello import subtract

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_hello_there():
    assert hello_there("Alice") == "Hello, Alice!"
    assert hello_there("Bob") == "Hello, Bob!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 2) == 0
    assert subtract(0, 5) == -5