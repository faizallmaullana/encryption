def encrypt(text, key):
    result = ""
    key_len = len(key)

    for i in range(len(text)):
        char = text[i]
        shift = key[i % key_len]

        if char.isupper():
            char = chr((ord(char) - ord('A') + ord(shift) - ord('A')) % 26 + ord('A'))
        elif char.islower():
            char = chr((ord(char) - ord('a') + ord(shift) - ord('a')) % 26 + ord('a'))

        result += char

    return result


def decrypt(text, key):
    result = ""
    key_len = len(key)

    for i in range(len(text)):
        char = text[i]
        shift = key[i % key_len]

        if char.isupper():
            char = chr((ord(char) - ord('A') + 26 - (ord(shift) - ord('A'))) % 26 + ord('A'))
        elif char.islower():
            char = chr((ord(char) - ord('a') + 26 - (ord(shift) - ord('a'))) % 26 + ord('a'))

        result += char

    return result


def main():
    print("Selamat datang di program enkripsi dan dekripsi menggunakan metode nilai geser yang rumit.")
    print("1. Enkripsi")
    print("2. Dekripsi")

    choice = int(input("Masukkan pilihan (1/2): "))

    input_text = input("Masukkan teks: ")
    key = input("Masukkan kunci: ")

    if choice == 1:
        encrypted_text = encrypt(input_text, key)
        print("Hasil enkripsi:", encrypted_text)
    elif choice == 2:
        decrypted_text = decrypt(input_text, key)
        print("Hasil dekripsi:", decrypted_text)
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
