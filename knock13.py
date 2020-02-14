with open("col1.txt") as col1_file,\
        open("col2.txt") as col2_file,\
        open("col3.txt",mode="w") as col3_file:
    for line1,line2 in zip(col1_file,col2_file):
        col3_file.write(line1.strip()+"\t"+line2.strip()+"\n")
