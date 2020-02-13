sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split(" ")
first_only = [1,5,6,7,8,9,15,16,19]
result = {}
for num,word in enumerate(words,1):
    if num in first_only:
        result[word[0]] = num
    else:
        result[word[0:2]] = num
print(result)