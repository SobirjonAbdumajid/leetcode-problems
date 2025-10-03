import pytest
# from solutions import even_index_chars, second_largest

# Fixture for even_index_chars
@pytest.fixture
def string_inputs():
    return [
        "PYnative",
        "Hello",
        "a",
        "",
        "Python3"
    ]
