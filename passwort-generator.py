import string
import random

def generate_random_password():
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!?@#$%|()^&~*")
    characters = list(string.ascii_letters + string.digits + "!?@#$%|()^&~*")

    while True:
        length = int(input("\nWie lang soll dein Passwort sein?: "))
        alphabets_count = int(input("Anzahl an Buchstaben: "))
        digits_count = int(input("Anzahl an Ziffern: "))
        special_characters_count = int(input("Anzahl an Sonderzeichen: "))
        
        characters_count = alphabets_count + digits_count + special_characters_count

        if characters_count > length:
            print("Die Gesamtzahl der Zeichen ist größer als die Länge des Passworts. Bitte versuche es erneut.")
        else:
            break

    password = [random.choice(alphabets) for _ in range(alphabets_count)]
    password.extend(random.choice(digits) for _ in range(digits_count))
    password.extend(random.choice(special_characters) for _ in range(special_characters_count))

    if characters_count < length:
        random.shuffle(characters)
        password.extend(random.choice(characters) for _ in range(length - characters_count))
    random.shuffle(password)

    print("\nHier ist dein neues Passwort: " + "".join(password) + "\n")
    input("Drücke Enter, um das Programm zu beenden.")
generate_random_password()
