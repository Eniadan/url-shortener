
from pwdlib import PasswordHash


# Uses a recommended secure password-hashing algorithm.
password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    # Convert the plain-text password into a secure hash
    # before storing it in the database.
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    # Check whether the submitted password matches the stored hash.
    return password_hash.verify(plain_password, hashed_password)
