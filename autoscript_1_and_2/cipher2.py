what_string = input('А теперь сам текст!  ')
while not what_string.isspace:
    what_string = input('Где то ты меня наебываешь. Попробуй еще раз.')


def spliting(text):
    t = text.split()


def ceasur(text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    for i in range(len(text)):
        alpha = 26
        low_alphabet = eng_lower_alphabet
        upp_alphabet = eng_upper_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])
            n = (place + 4) % alpha

            if text[i] == text[i].lower():
                print(low_alphabet[n], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[n], end='')

        else:
            print(text[i], end='')


ceasur(what_string)
