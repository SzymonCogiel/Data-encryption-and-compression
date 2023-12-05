import utils


def generate_polibiusz_tab(key):
    u_key = utils.unique_string_to_list(key)
    u_alf = utils.unique_alfabet(utils.alfabet.copy(), u_key)
    u_alf.remove('J')
    flat_list = u_key + u_alf
    return [flat_list[i:i + 5] for i in range(0, len(flat_list), 5)]


def generate_polibiusz_hash_tab(polibiusz_tab):
    polibiusz_hash_tab = {val: (i + 1, j + 1) for i, row in enumerate(polibiusz_tab) for j, val in enumerate(row)}
    return polibiusz_hash_tab


@utils.replace_j
@utils.uppercase_strings
def polibiusz(text, key):
    polibiusz_tab = generate_polibiusz_tab(key)
    polibiusz_hash_tab = generate_polibiusz_hash_tab(polibiusz_tab.copy())
    return list(map(lambda c: polibiusz_hash_tab[c], [*text]))
