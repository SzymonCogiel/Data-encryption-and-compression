import utils
from encryption.polibiusz import generate_polibiusz_tab, generate_polibiusz_hash_tab


@utils.uppercase_strings
def playfair(text, key):
    polibiusz_tab = generate_polibiusz_tab(key)
    polibiusz_hash_tab = generate_polibiusz_hash_tab(polibiusz_tab)
    splited_text = [text[i:i + 2] for i in range(0, len(text), 2)]
    if len(text) % 2 != 0:
        splited_text[-1] += key[0]
    encrypted_text = []
    for c1, c2 in splited_text:
        y1, x1 = polibiusz_hash_tab[c1]
        y2, x2 = polibiusz_hash_tab[c2]
        if x1 == x2:
            y1 += 1
            y2 += 1
            if y1 > 5:
                y1 = 1
            if y2 > 5:
                y2 = 1
        elif y1 == y2:
            x1 += 1
            x2 += 1
            if x1 > 5:
                x1 = 1
            if x2 > 5:
                x2 = 1
        else:
            x1, x2 = x2, x1
        encrypted_text.append(polibiusz_tab[y1 - 1][x1 - 1] + polibiusz_tab[y2 - 1][x2 - 1])
    return encrypted_text
