import random
import string

def generate():
    suffix = "".join([random.choice(string.ascii_letters) for i in range(5)])
    return suffix