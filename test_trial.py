### WRITE IMPORT STATEMENTS HERE-
import test
import pytest

sentence = "Trying to master the use of GitHub Classroom."
@pytest.fixture
def input_value():
    input = sentence
    return input

# First test function test_length()
def test_length(input_value):

    assert test.word_count(input_value) == 8
    assert test.char_count(input_value) == 45

    #raise NotImplementedError()

# Second test function test_struc()
def test_struc(input_value):
   
    assert test.first_char(input_value) == "T"
    assert test.last_char(input_value) == "."

#raise NotImplementedError()
# Run these tests with `python3 -m pytest test_spellcheck.py`

