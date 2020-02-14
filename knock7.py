def template(x,y,z):
    return "{h}時の{t}は{v}".format(h=x,t=y,v=z)

print(template(12,"気温",22.4))