fname = "hightemp.txt"
with open(fname,encoding="utf-8") as data_file:
    lines = data_file.readlines()
    kens = [line.split("\t")[0] for line in lines]
    kens.sort()
    pre_ken = kens[0]
    ken_num = {}
    count = 1
    for ken in kens:
        if pre_ken == ken:
            count += 1
        else:
            ken_num[ken] = count
            count = 1
            pre_ken = ken

ken_num_sorted = sorted(ken_num.items(),key= lambda x:x[1],reverse = True)
for ken,num in ken_num_sorted:
    print(ken + ":",num)

