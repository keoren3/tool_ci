import pytest

from flask_app import hello


def test_should_return_hello_from_python():
    assert "Hello from Python!" == hello()
