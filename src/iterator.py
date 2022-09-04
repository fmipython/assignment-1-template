class Iterator:
    """Iterator allows consuming items from a list 1 by one

    The simplest way to think of it is a list and a pointer,
    which points the current element. Upon consumption of the
    current element the pointer is shifted 1 position and points
    the next element in the list

    An iterator allows us to go over a list of items like a for loop
    but we can pause at certain places

    e.g.
    iter = Iterator([1,2,3,4,5,6])
    iter.next() # skip 1
    
    for i in range(2):
        print(iter.next()) # prints 2 and 3
    
    iter.next() # skip 4
    
    while item := iter.next():
        print(item) # prints the rest of the items: 5 and 6
    """
    
    def __init__(self, tokens):
        """Initialize a new Iterator from the tokens
        """
        pass

    def next(self):
        """Return the next token if such exists, None otherwise
        """
        pass

    def map(self, func):
        """Apply a function to all tokens in the iterator
        """
        pass

    def filter(self, func):
        """
        For every element if func returns True, keep it
        Otherwise, remove it from the tokens
        """
        pass

    def advance(self, positions):
        """Move the iterator positions-number of tokens ahead
        """
        pass

def from_list(arr):
    """Construct an iterator from a list of items
    """
    pass

def from_tokenizer(tokenizer):
    """Construct an iterator from a tokenizer
    """
    pass
