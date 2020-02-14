fname = "hightemp.txt"
count= 0
with open(fname,encoding="utf-8") as data:
    for line in data:
        print(line.replace("\t"," "),end="")