import string
import os


def letters_file_line(n):
    for i in range(n):
        with open("words%s.txt" % i, "w") as f:
            alphabet = string.ascii_uppercase
            for i in range(0, len(alphabet), n):
                letters = [alphabet[i:i + n] + "\n"]
                f.writelines(letters)
        os.system('git add .')
        os.system('git commit -m "%s"' % i)
    os.system('git push')


letters_file_line(30)
