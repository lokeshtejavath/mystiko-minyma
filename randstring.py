import random as rand
import secrets
import string


def randstring(keylength: int = 25) -> str:
    key = str(rand.randint(1, 255))
    qualifier = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(keylength))
    while len(key) < 3:
        key = "0" + key
    return key+qualifier


# print(randstring())
