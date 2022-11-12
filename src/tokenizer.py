"""Tokenizer accepts a string and converts it to a list of tokens
"""

class Tokenizer:
    """Tokenizer accepts a string and converts it to a list of tokens

    A token might be a keyword, a symbol, an arbitrary string, a number, etc.
    A token is:
    - anything surrounded by single or double quotes
    - a symbol
    - a word surrounded by symbols/spaces
    A token is not:
    - any space outside quotes ('    word   ' is trimmed down to 1 token - [word])

    Assumptions: We will never have quotes inside quotes. e.g. '"' will never be
    given as an input, so don't worry about parsing nested quotes. Also, text in
    quotes will have no espace symbols, i.e. we won't have ' .. \' ..' as input.

    The symbols are: ()[]{},.;:
    The spaces are: ' ' (space), \n (new line), \t (tab)

    Examples:

    Raw: 'hello world' and python
    Result: ['hello world', 'and', 'python']
    Explanation: anything inside quotes is one token

    Raw:        +/word
    Result: ['+', '/', 'word']
    Explanation: empty spaces are ignored and symbols are separated from words and other symbols

    Raw: int main(char[])
    Result: ['int', 'main', '(', 'char', '[', ']', ')']
    """

    def __init__(self):
        """Initialize a tokenizer
        """

    def from_string(self, string):
        """Update the state of the tokenizer to use the given input string

        The tokenization can happen here or in get_all, either is fine

        :param str string: string to be tokenized
        :return: a string with error message if the brackets are unbalanced
            or there are unclosed quotes, None otherwise
        """

    def get_all(self):
        """Return all tokens

        :return: all the tokens that the tokenizer parsed from
            the string argument provided in the from_string method
            Return an empty list if errors occurred during tokenization
        :rtype: list
        """
