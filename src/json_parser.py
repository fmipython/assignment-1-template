"""Json constructs dicts/lists of objects from a json string given as an Iterator
"""

# pylint: disable=R0903
class Json:
    """Json constructs dicts/lists of objects from a json string given as an Iterator

    This is a simplified JSON parser.
    For the formal specification of JSON see https://www.json.org/json-en.html

    A json object looks like
    (source: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON):
    {
        "squadName": "Super hero squad",
        "formed": 2016,
        "active": true,
        "members": [
            {
                "name": "Eternal Flame",
                "age": 1000000,
                "powers": [
                    "Immortality",
                    "Inferno"
                ]
            }
        ]
    }

    A lot like a python dictionary :)

    JSON rules
    - objects and lists can be nested inside each other
    - a list contains a collection of sequential items with arbitrary types
    - a dict contains a collection of key:value pairs, the key is always a string,
        while the value is a primitive type or a dict or a list
    - the primitive types are:
        - string - anything inside single/double quotes
        - number - floating point number (also used for integers)
        - bool - true/false
        - null - None (we won't use those)

    { denotes the start of an object (dict)
    } denotes the end of the current object
    [ denotes the start of a list
    ] denotes the end of the current list
    """

    def __init__(self, iterator):
        """Construct a Json parser from an iterator

         :param iterator Iterator: Iterator, which to consume during compilation
        """

    def compile(self):
        """Consume all tokens in the iterator to compile a Json object/array

        :return: (json object, error), where the json object could be a dict or a list

        Assumptions: The input will always be valid JSON (the error should always be None)

        Strings should remain strings
        The keywords true and false (case-insensitive) should be converted to the
            boolean True and False respectively
        Numbers should be converted to floats (both integers and floating point numbers)
        """
