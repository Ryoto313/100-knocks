fname = "hightemp.txt"
n = int(input('N--> '))
with open(fname,encoding="utf-8") as data_file:
    lines = data_file.readlines()
    for i,line in enumerate(lines):
        if i >= n:
            break
        else:
            print(line.rstrip())

