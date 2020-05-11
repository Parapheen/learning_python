from simplecrypt import encrypt, decrypt

with open("advanced_stepik/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open('advanced_stepik/passwords.txt', 'r') as pasw:
    for line in pasw:
        pw = line.strip()
        try:
            print(decrypt(pw, encrypted))
        except Exception:
            print(Exception)
