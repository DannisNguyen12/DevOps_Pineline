from hello import hello_world
from hello import hello_there

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_hello_there():
    assert hello_there("Alice") == "Hello, Alice!"
    assert hello_there("Bob") == "Hello, Bob!"