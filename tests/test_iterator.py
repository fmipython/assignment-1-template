from src.iterator import Iterator
from src.tokenizer import Tokenizer
import src.iterator as iterator

def test_from_list():
    iter = iterator.from_list(['1', '2'])
    assert iter.next() == '1'
    assert iter.next() == '2'

def test_from_tokenizer():
    tokenizer = Tokenizer()
    tokenizer.from_string('main()')
    iter = iterator.from_tokenizer(tokenizer)
    assert iter.next() == 'main'
    assert iter.next() == '('
    assert iter.next() == ')'

def test_constructor():
    iter = Iterator(['1', '2'])
    assert iter.next() == '1'
    assert iter.next() == '2'

def test_next_none():
    iter = Iterator(['1', '2'])
    assert iter.next() == '1'
    assert iter.next() == '2'
    assert iter.next() == None

def test_map():
    iter = Iterator(['1', '2'])
    iter.map(int)
    assert iter.next() == 1
    iter.map(str)
    assert iter.next() == '2'

def test_filter():
    iter = Iterator(['1', '2', 3, 4])
    iter.filter(lambda x: type(x) == type(42))
    assert iter.next() == 3
    assert iter.next() == 4
    assert iter.next() == None

def test_advance():
    iter = Iterator(['1', '2', '3', '4'])
    assert iter.next() == '1'
    iter.advance(2)
    assert iter.next() == '4'
    assert iter.next() == None

    iter = Iterator(['1'])
    iter.advance(100)
    assert iter.next() == None
    iter.advance(100)
    assert iter.next() == None
