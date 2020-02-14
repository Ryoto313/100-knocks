def ngram(n,target):
    result = []
    for i in range(0,len(target)-n+1):
        result.append(target[i:i+n])
    return result

target = "I am an NLPer"

#単語bi-gram
print(ngram(2,target.split(" ")))

#文字bi-gram
print(ngram(2,target))


