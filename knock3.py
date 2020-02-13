sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.split(" ")

print(words)
l = []
for word in words:
    num = (len(word) - word.count(",")-word.count("."))
    l.append(num)
print(l)