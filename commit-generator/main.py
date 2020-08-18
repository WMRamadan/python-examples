import string
import os


def letters_file_line(n):
   with open("words1.txt", "w") as f:
        alphabet = string.ascii_uppercase
        for i in range(0, len(alphabet), n):
            letters = [alphabet[i:i + n] + "\n"]
            f.writelines(letters)
            os.system('git add .')
            os.system('git commit -m "%s"' % i)


letters_file_line(3)
