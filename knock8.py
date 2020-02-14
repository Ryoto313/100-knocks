def cipher(target):
    result=""
    for i in target:
        if i.islower():
            result += chr(219-ord(i))
        else:
            result += i
    return result

target = "I want to be a hair dresser!"
print("元の文：",target)
print("暗号化後:",cipher(target))
print("複合化後:",cipher(cipher(target)))