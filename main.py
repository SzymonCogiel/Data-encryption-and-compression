from encryption.cezar import cezar
from encryption.vigenere import vigenere
from encryption.polibiusz import polibiusz
from encryption.playfair import playfair
from compression.lzw import LZW


def main():
    print("===============SZYFROWANKO I KOPRESJA DANYCH Z MLYNAREM======================")
    print("1) Cezar z maslem")
    print("2) Oliva Vigenere")
    print("3) Polibisz")
    print("4) Playfair")
    try:
        choice = int(input('Podaj opcje: \n'))
    except ValueError:
        print('ValueError: choice must be int')
        try:
            choice = int(input('Spróbuj podac opcje jeszcze raz: \n'))
        except Exception as e:
            print(str(e))
            return -1
    match choice:
        case 1:
            print('Zaszyfrowana wiadomosc Cezarem to: ',
                  cezar(text=input('Podaj tekst: \n'), key=input('Podaj haslo: \n'),
                        position=int(input('Podaj pozycje: \n'))))
        case 2:
            print('Zaszyfrowana wiadomosc Vigenere to: ',
                  vigenere(text=input('Podaj tekst: \n'), key=input('Podaj haslo: \n')))
        case 3:
            print('Zaszyfrowana wiadomosc Polibiuszem to: ',
                  *polibiusz(input('Podaj tekst: \n'), input('Podaj haslo: \n')))
        case 4:
            print('Zaszyfrowana wiadomosc Playfairem to: ',
                  *playfair(input('Podaj tekst: \n'), input('Podaj haslo: \n')))
        case 5:
            print('Kompresja wiadomosc LZW to: ',
                  *LZW().compression(input('Podaj tekst: \n')))
        case _:
            print('Nie ma takiego numeru')


if __name__ == '__main__':
    main()
