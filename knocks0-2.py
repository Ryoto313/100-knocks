
# knock0
a = "stressed"
b = a[::-1]
print(b)

# knock1
a = "パタトクカシー"
b = a[::2]
print(b)

# knock2
a = "パトカー"
b = "タクシー"
c = ""
for i,j in zip(a,b):
    c += i + j
print(c)

# knock3
words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = words.split(" ")
print(l)