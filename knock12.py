fname = "hightemp.txt"
count= 0
with open(fname,encoding="utf-8") as data_file,\
        open("col1.txt",mode="w") as col1_file,\
        open("col2.txt", mode="w") as col2_file:
    for line in data_file:
        cols = line.split("\t")
        col1_file.write(cols[0]+"\n")
        col2_file.write(cols[1]+"\n")