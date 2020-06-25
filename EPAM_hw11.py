import pytest
from homework4_2 import count_words


def test_count_words_positive():
    assert count_words(['epam-pam-pam', 'param-pam-bam'], 'pam') == 4


def test_count_words_zero():
    assert count_words(['intel', 'mera', 'microsoft'], 'epam') == 0

def test_count_words_bad_input():
    with pytest.raises(TypeError) as e:
        count_words(22, 'pam')
    assert str(e.value)=="\'int\' object is not iterable"

"""
coverage report
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
2.py                                                          10      0   100%
homework4_2.py                                                 5      0   100%

"""
