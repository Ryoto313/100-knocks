fname = "hightemp.txt"
with open(fname,encoding="utf-8") as data_file:
    lines = data_file.readlines()
    lines.sort(key=lambda x:float(x.split("\t")[2]),reverse=True)
    for line in lines:
        print(line,end="")