import string
from random import choice


with open("data-files/examples/large_data.txt", "w") as fh:
    i = 1
    while i <= 130000:
        word = (
            ''.join(
                choice(string.ascii_uppercase + string.digits)
                for _ in range(100)) + "|") * 100
        fh.write(word[:-1] + "\n")
        i += 1
