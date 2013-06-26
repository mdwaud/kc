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
    >>> pig_latinize("crevice")
    'evicecray'
    """
    # handle some simple base cases
    if len(word) < 3 or word.upper() in IGNORE_LIST:
        return word
    # check for the first vowel
    for index, letter in enumerate(word):
        if letter.upper() in VOWELS:
            return word[index:] + word[:index] + "ay"
    # no vowels, so just return what we got
    return word


if __name__ == "__main__":
    import doctest
    doctest.testmod()