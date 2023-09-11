name = "maciek"

def display_name():
    name = "kurdziel"
    print(name)

display_name()
print(name)

def sumnumber(*args):    #*args to funckja która przymuję nieograniczoną ilość argumentów, jest krotką
    i = 0
    args = list(args)
    args[0] = 0
    for x in args:
        i += x
    return i

print(sumnumber(25,2,3,4,5,7,))
