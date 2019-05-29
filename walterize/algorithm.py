class WalterizeException(ValueError):
    pass


def walterize(word):
    vowels = ["a", "i", "o", "u", "y"]
    word = word.lower()
    if len(word) < 3:
        return word
    last_char = word[-1:]
    if last_char == "p":
        return "{}pese".format(word)
    if last_char == "e":
        return "{}se".format(word)
    if word[-3:] == "ops":
        return "{}pese".format(word[:-1])
    if last_char in vowels:
        return "{}ppese".format(word)
    return "{}ese".format(word)


def walterize_phrase(words):
    if not words:
        raise WalterizeException
    return " ".join((walterize(word) for word in words))
