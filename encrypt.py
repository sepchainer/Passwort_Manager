import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

chunks = 32 * 1024


def encrypt(key, filename):
    out_filename = "encrypted!" + os.path.basename(filename)
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CFB, IV)
    with open(filename, 'rb') as f_input:
        with open(out_filename, 'wb') as f_output:
            f_output.write(file_size.encode('utf-8'))
            f_output.write(IV)
            while True:
                chunk = f_input.read(chunks)
                if len(chunk) == 0:
                    break
                if len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                f_output.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    out_filename = filename.split("!")[-1]
    with open(filename, 'rb') as f_input:
        file_size = int(f_input.read(16))
        IV = f_input.read(16)
        decryptor = AES.new(key, AES.MODE_CFB, IV)
        with open(out_filename, 'wb') as f_output:
            while True:
                chunk = f_input.read(chunks)
                if len(chunk) == 0:
                    break
                f_output.write(decryptor.decrypt(chunk))
                f_output.truncate(file_size)


def get_key(password):
    hashing = SHA256.new(password.encode('utf-8'))
    return hashing.digest()
