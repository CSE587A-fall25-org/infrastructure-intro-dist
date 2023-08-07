from gradescope_utils.autograder_utils.decorators import weight
from infrastructure_intro.assignment import hello_world

@weight(3)
def test_hello_world():
    """Test the hello world function"""
    assert hello_world() == "hello world"