def ngram(n,target):
    result = []
    for i in range(0,len(target)-n+1):
        result.append(target[i:i+n])
    return result

X = set(ngram(2,"paraparaparadise"))
Y = set(ngram(2,"paragraph"))
set_or = X|Y
print("和集合",set_or)
set_and = X&Y
print("積集合",set_and)
set_sub = X-Y
print("差集合",set_sub)
print("se" in set_or)
