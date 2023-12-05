import utils


@utils.uppercase_strings
def cezar(text, key, position):
    u_key = utils.unique_string_to_list(key)
    u_alf = utils.unique_alfabet(utils.alfabet.copy(), u_key)
    thresh = len(utils.alfabet) - (position + len(u_key) - 1)
    if thresh > 0:
        last, first = u_alf[:thresh], u_alf[thresh:]
        alfabet_cor = first + u_key + last
    else:
        thresh_2 = len(utils.alfabet) - position + 1
        last, first = u_key[:thresh_2], u_key[thresh_2:]
        alfabet_cor = first + u_alf + last
    slownik = dict(zip(utils.alfabet, alfabet_cor))
    return ''.join(map(lambda s: slownik[s], [*text]))
