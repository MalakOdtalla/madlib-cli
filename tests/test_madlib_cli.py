import pytest
from madlib_cli.madlib import read_templet,parse_templet,merge

def test_read_template():
    actual=read_templet("../assests/input.txt")
    expected=open('../assests/input.txt','r').read()
    assert actual == expected


def test_parse_template():
    actual = parse_templet("I the {Adjective } and {Adjective} {A First Name}")
    expected = (['Adjective', 'Adjective', 'A First Name'], 'I the  {} and  {}  {}')
    assert expected == actual

def test_merge():
    actual= merge("It was a {} and {} {}.",["dark","stormy","night"])
    expected="It was a dark and stormy night."
    assert actual == expected
