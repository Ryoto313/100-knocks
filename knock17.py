fname = "hightemp.txt"
with open(fname,encoding="utf-8") as data_file:

    set_ken = set()
    for line in data_file:
        cols = line.split("\t")
        set_ken.add(cols[0])

for i in set_ken:
    print(i)