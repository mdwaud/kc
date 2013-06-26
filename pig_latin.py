VOWELS = "aeiouy"

def pig_latinize(raw_word):
    """
    Return a pig latin-ized version of a word

    >>> pig_latinize("happy")
    'appyhay'
    >>> pig_latinize("duck")
    'uckday'
    >>> pig_latinize("egg")
    'eggyay'
    >>> pig_latinize("thbbbt")
    'thbbbtay'
    """
    word = raw_word.lower()
    # check for the first vowel
    for index, letter in enumerate(word):
        if letter in VOWELS:
            if index > 0:
                return word[index:] + word[:index] + "ay"
            else:
                return word + "yay"
    # no vowels... let's just add an "ay"
    return word + "ay"


if __name__ == "__main__":
    import doctest
    doctest.testmod()