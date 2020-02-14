import random
def shuffle(target):
    words = target.split(" ")
    result = []
    for i in words:
        if len(i) > 4:
            i_list = list(i[1:-1])
            random.shuffle(i_list)
            new_i = i[0]+"".join(i_list)+i[-1]
        else:
            new_i = i

        result.append(new_i)

    return " ".join(result)
target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(shuffle(target))
