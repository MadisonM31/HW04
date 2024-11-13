# Madison Manning
# UWYO COSC 1010
# 11/12/2024
# HW 04
# Lab Section: 10

from pathlib import Path 
imp_path = Path("prompt.txt")
imp_prompt = imp_path.read_text()
lines = imp_prompt.splitlines()

orders = []
config = ""

for line in lines:
    orders = line.split('\t')
    for order in orders:
        num = order[2:]
        if len(order) > 0:
            if order[0] == "w":
                config += " " * int(num)
            else:
                config += "*" * int(num)
    config += "\n"

out_path = Path("out.txt")
out_path.write_text(config)





