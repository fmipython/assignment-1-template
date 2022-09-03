from src.tokenizer import Tokenizer

def test_empty_string_produces_no_tokens():
    t = Tokenizer()

    t.from_string('')
    assert t.get_all() == []

def test_parsing_brackets():
    t = Tokenizer()
    t.from_string('main(param){array[1]}')
    assert t.get_all() == ['main', '(', 'param', ')', '{', 'array', '[', '1', ']', '}']

def test_parsing_quotes():
    t = Tokenizer()
    t.from_string('"string inside quotes"')
    assert t.get_all() == ['string inside quotes']

    t.from_string("""1"double quotes"2'single quotes'3""")
    assert t.get_all() == ['1', 'double quotes', '2', 'single quotes', '3']

def test_parsing_spaces():
    t = Tokenizer()
    t.from_string('1 2\t3\n4     5')
    assert t.get_all() == ['1', '2', '3', '4', '5']

def test_parsing_symbols():
    t = Tokenizer()

    t.from_string(',1,2,')
    assert t.get_all() == [',', '1', ',',  '2', ',']

    t.from_string(';1;2;')
    assert t.get_all() == [';', '1', ';', '2', ';']

def test_parse_json():
    t = Tokenizer()

    t.from_string("""
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
    """)
    assert t.get_all() == [
            '{',
                'course', ':', 'Python', ',',
                'lecturers', ':', '[',
                    'Lyuboslav Karev', ',',
                    'Alexander Ignatov',
                ']', ',',
                'moral support', ':', 'Ivan Luchev', ',',
                'active', ':', 'true', ',',
                'started_year', ':', '2022',
            '}',
        ]

def test_error_bracket_balance():
    t = Tokenizer()

    err = t.from_string('[](){}')
    assert err is None

    err = t.from_string('{([][]()){[[]()]}}()')
    assert err is None

    err = t.from_string('{')
    assert err is not None

    err = t.from_string('{([][])){[[]()]}}()')
    assert err is not None

def test_error_quotes_unclosed():
    t = Tokenizer()
    err = t.from_string('"the quotes are not closed')
    assert err is not None

def test_get_all_after_error_is_empty():
    t = Tokenizer()

    t.from_string('word "')
    assert t.get_all() == []

    t.from_string('((')
    assert t.get_all() == []

def test_from_string_resets_state():
    t = Tokenizer()

    t.from_string('one')
    assert t.get_all() == ['one']

    t.from_string('two')
    assert t.get_all() == ['two']
