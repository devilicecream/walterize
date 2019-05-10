def walterize(word):
    vowels = ['a', 'i', 'o', 'u', 'y']
    word = word.lower()
    last_char = word[-1:]
    if last_char == 'p':
        return "{}pese".format(word)
    if last_char == 'e':
        return "{}se".format(word)
    if word[-3:] == 'ops':
        return "{}pese".format(word[:-1])
    if last_char in vowels:
        return "{}ppese".format(word)
    return "{}eppese".format(word)
