VOWELS = "AEIOUY"
IGNORE_LIST = ["THE",]

def pig_latinize(word):
    """
    Return a pig latin-ized version of a word

    >>> pig_latinize("Python")
    'ythonPay'
    >>> pig_latinize("The")
    'The'
    >>> pig_latinize("my")
    'my'
    >>> pig_latinize("amber")
    'amberay'
    """
    if len(word) < 3 or word.upper() in IGNORE_LIST:
        return word

    for index, letter in enumerate(word):
        if letter.upper() in VOWELS:
            return word[index:] + word[:index] + "ay"
    return word


if __name__ == "__main__":
    import doctest
    doctest.testmod()