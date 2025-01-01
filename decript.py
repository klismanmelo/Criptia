from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from keys import load_keys_from_file


def decrypt():
        with open('encrypted.bin', 'rb') as f:
            iv = f.read(16)
            decrypt_data = f.read()
        key = load_keys_from_file()
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
        return original.decode('utf-8')