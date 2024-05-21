from aes_encryption import generate_aes_key, encrypt_aes, decrypt_aes
from rsa_encryption import generate_rsa_keys, encrypt_rsa, decrypt_rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def hash_sha256(data):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data)
    hashed_data = digest.finalize()
    return hashed_data

if __name__ == "__main__":
    # AES example
    aes_key = generate_aes_key()
    aes_plaintext = input("Enter message for AES encryption: ").encode()
    aes_ciphertext = encrypt_aes(aes_key, aes_plaintext)
    print("AES Encrypted:", aes_ciphertext)
    aes_decrypted = decrypt_aes(aes_key, aes_ciphertext)
    print("AES Decrypted:", aes_decrypted.decode())

    # RSA example
    rsa_private_key, rsa_public_key = generate_rsa_keys()
    rsa_plaintext = input("Enter message for RSA encryption: ").encode()
    rsa_ciphertext = encrypt_rsa(rsa_public_key, rsa_plaintext)
    print("RSA Encrypted:", rsa_ciphertext)
    rsa_decrypted = decrypt_rsa(rsa_private_key, rsa_ciphertext)
    print("RSA Decrypted:", rsa_decrypted.decode())

    # SHA-256 example
    data = input("Enter data to be hashed: ").encode()
    hashed_data = hash_sha256(data)
    print("SHA-256 Hashed:", hashed_data.hex())
