from typing import List
from collections import deque

alfabet_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alfabet = [*alfabet_str]


def uppercase_strings(func):
    def wrapper(*args, **kwargs):
        args = [arg.upper() if isinstance(arg, str) else arg for arg in args]
        kwargs = {key: value.upper() if isinstance(value, str) else value for key, value in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper


def vigenere_tab():
    vige_tab = {}
    for i, c in enumerate(alfabet.copy()):
        alf = deque(alfabet)
        alf.rotate(-i)
        vige_tab[c] = list(alf)
    return vige_tab


def unique_string_to_list(s: str) -> List[str]:
    ulist = []
    for c in s:
        if c not in ulist:
            ulist.append(c)
    return ulist


def unique_alfabet(alf: List[str], key: List[str]) -> List[str]:
    for c in key:
        alf.remove(c)
    return alf


def replace_j(func):
    def wrapper(*args, **kwargs):
        args = tuple(arg.replace('j', 'i') if isinstance(arg, str) else arg for arg in args)
        kwargs = {key: value.replace('j', 'i') if isinstance(value, str) else value for key, value in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper
