from app.main import greet

def test_greet():
    assert greet("CI/CD") == "Hello, CI/CD!"