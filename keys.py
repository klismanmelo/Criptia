from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

def save_keys_to_file(password, key_file="keys.bin"):
    simple_key = get_random_bytes(16)
    key = PBKDF2(password, simple_key, dkLen=32)

    with open(key_file, "wb") as f:
        f.write(key)

def load_keys_from_file(key_file="keys.bin"):

    with open(key_file, "rb") as f:
        key = f.read()

    return key
