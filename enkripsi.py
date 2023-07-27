from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(data, password):
    salt = get_random_bytes(16)
    kdf = PBKDF2(password, salt, dkLen=32, count=100000)  # Key derivation function
    key = kdf[:16]  # AES-128 requires a 16-byte key
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return salt, iv, ct

def decrypt(salt, iv, ct, password):
    kdf = PBKDF2(password, salt, dkLen=32, count=100000)
    key = kdf[:16]
    ct = base64.b64decode(ct)
    iv = base64.b64decode(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

def main():
    password = input("Masukkan kunci enkripsi yang rumit: ")
    data = input("Masukkan teks yang ingin dienkripsi: ")

    salt, iv, ciphertext = encrypt(data, password)
    print("Teks terenkripsi:", ciphertext)

    decrypted_text = decrypt(salt, iv, ciphertext, password)
    print("Teks terdekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
