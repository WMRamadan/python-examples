import jc
import subprocess

table = ""
output = subprocess.check_output("docker ps", shell=True)

for row in output.split(b"\n"):
    table += row.decode("utf-8") + "\n"

data = jc.parse('asciitable', table)
print(data)
