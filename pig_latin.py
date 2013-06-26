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
    for index, letter in enumerate(word):
        if letter in VOWELS:
            if index > 0:
                # first letter is not a vowel
                return word[index:] + word[:index] + "ay"
            else:
                # first letter is a vowel
                return word + "yay"
    # no vowels... let's just add an "ay"
    return word + "ay"


if __name__ == "__main__":
    import doctest
    doctest.testmod()