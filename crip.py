from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from keys import load_keys_from_file
def criptography(message):
    key = load_keys_from_file()
    cipher = AES.new(key, AES.MODE_CBC)
    cipherdata = cipher.encrypt(pad(message, AES.block_size))
    try:
        with open('encrypted.bin', 'wb') as f:
            f.write(cipher.iv)
            f.write(cipherdata)
            print('All right')
    except:
        print('Failed to save encrypted data')

