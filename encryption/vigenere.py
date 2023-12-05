import utils

v_tab = utils.vigenere_tab()


@utils.uppercase_strings
def vigenere(text, key):
    return ''.join([v_tab[key[i % len(key)]][utils.alfabet.index(c)] for i, c in enumerate(text)])
