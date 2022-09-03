from src.json_parser import Json
from src.tokenizer import Tokenizer
from src.iterator import Iterator


def test_simple_object():
    json = """
        {
          'course': 'Python',
          'category': 'Programming'
        }
    """

    tokenizer = Tokenizer()
    tokenizer.from_string(json)
    iterator = Iterator(tokenizer.get_all())
    compiler = Json(iterator)

    want_result = {
      'course': 'Python',
      'category': 'Programming'
    }

    actual, err = compiler.compile()
    assert err is None
    assert actual == want_result

def test_primitive_types():
    json = """
        {
          'string': 'this is a string',
          'number': '4.42',
          'number again': '4',
          'false': false,
          'true': true
        }
    """

    tokenizer = Tokenizer()
    tokenizer.from_string(json)
    iterator = Iterator(tokenizer.get_all())
    compiler = Json(iterator)

    want_result = {
          'string': 'this is a string',
          'number': 4.42,
          'number again': 4,
          'false': False,
          'true': True,
    }

    actual, err = compiler.compile()
    assert err is None
    assert actual == want_result

def test_nested_items():
    json = """
        {
          'client': {
            'first_name': 'Foo',
            'last_name': 'Bar'
          }
        }
    """

    tokenizer = Tokenizer()
    tokenizer.from_string(json)
    iterator = Iterator(tokenizer.get_all())
    compiler = Json(iterator)

    want_result = {
        'client': {
            'first_name': 'Foo',
            'last_name': 'Bar'
        }
    }

    actual, err = compiler.compile()
    assert err is None
    assert actual == want_result

def test_root_is_list():
    json = """
        [
          'string',
          'number',
        ]
    """

    tokenizer = Tokenizer()
    tokenizer.from_string(json)
    iterator = Iterator(tokenizer.get_all())
    compiler = Json(iterator)

    want_result = ['string', 'number']

    actual, err = compiler.compile()
    assert err is None
    assert actual == want_result

def test_full_json():
    json = """
        {
          "course": "Python",
          "lecturers": [
              "Lyuboslav Karev",
              "Alexander Ignatov"
          ],
          "moral support": "Ivan Luchev",
          "active": true,
          "started_year": 2022
        }
    """

    tokenizer = Tokenizer()
    tokenizer.from_string(json)
    iterator = Iterator(tokenizer.get_all())
    compiler = Json(iterator)

    want_result = {
      "course": "Python",
      "lecturers": [
          "Lyuboslav Karev",
          "Alexander Ignatov"
      ],
      "moral support": "Ivan Luchev",
      "active": True,
      "started_year": 2022
    }

    actual, err = compiler.compile()
    assert err is None
    assert actual == want_result

