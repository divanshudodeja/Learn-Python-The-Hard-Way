from nose.tools import assert_equal
from ex49 import ex49

def test_peek():
    assert_equal(ex49.peek([('verb', 'go')]), 'verb')
    assert_equal(ex49.peek([]), None)

def test_match():
    assert_equal(ex49.match([], 'verb'), None)
    assert_equal(ex49.match([('verb', 'go')], 'verb'), ('verb', 'go'))

def test_parse_verb():
    assert_equal(ex49.parse_verb([('verb', 'go')]) , ('verb', 'go'))