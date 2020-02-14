fname = "hightemp.txt"
n = int(input('N--> '))
with open(fname,encoding="utf-8") as data_file:
    lines = data_file.readlines()
    show_lines = lines[-n:]
    for line in show_lines:
        print(line.rstrip())