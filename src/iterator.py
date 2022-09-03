class Iterator:
    def __init__(self, tokens):
        """
        Initialize a new Iterator from the tokens
        """
        pass

    def next(self):
        """
        Return the next token if such exists, None otherwise
        """
        pass

    def map(self, func):
        """
        Apply a function to all tokens in the iterator
        """
        pass

    def filter(self, func):
        """
        For every element if func returns True, keep it
        Otherwise, remove it from the tokens
        """
        pass

    def advance(self, positions):
        """
        Move the iterator positions-number of tokens ahead
        """
        pass

def from_list(arr):
    """
    Construct an iterator from a list of items
    """
    pass

def from_tokenizer(tokenizer):
    """
    Construct an iterator from a tokenizer
    """
    pass
