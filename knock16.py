fname = "hightemp.txt"
n = int(input('N--> '))
with open(fname,encoding="utf-8") as data_file:
    lines = data_file.readlines()
    base_unit = len(lines)//n
    add_1_iter = len(lines) - n*base_unit
    index = 0
    for i in range(1,n+1):
        if i <= add_1_iter:
            unit = base_unit + 1
        else:
            unit = base_unit
        with open("child{num}.txt".format(num=i), mode="w", encoding="utf-8") as child_file:
            for line in lines[index:index+unit]:
                child_file.write(line.rstrip() + "\n")

        index = index + unit


