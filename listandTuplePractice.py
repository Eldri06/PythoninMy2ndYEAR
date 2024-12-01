from sty import Style, RgbFg

print("\n--- List ---")

list = ['eldrian', 23, 'jake', 25, 'celine']
tinylist = ['John', 1738]
list[1] = 'gwapo'

print(list)
print(tinylist)
print(list[3])
print(list[1:4])
print(list[2:])
print(list * 2)
print(list + tinylist)


print("\n--- Tuple ---")
tuple = ('abcdefgh', 1234, 'johnny', 69.9)
tinytuple = ('abcde', 99)

print(tuple)
print(tinytuple)
print(tuple[2])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 4)
print(tuple + tinytuple)


print("\n--- Dictionary ---")
dict = {}
dict['one'] = 'This is one'
dict[2]     = 'This is two'

tinydict = {'name': 'eldrian', 'code': 2042, 'dept' : 'dase'}

print(dict['one'])
print(dict[2])
print([tinydict])
print([tinydict.keys()])
print([tinydict.values()])


print("\n--- Python String Methods ---")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

txtt = "my name is eldrian"
print(txtt.upper())


txttt = "MY NAME IS ELDRIAN"
print(txtt.lower())


ttxttt = "MY NAME IS ELDRIAN"
print(ttxttt.split())
print(ttxttt[1:4])

tttxttt = "my name is eldrian"
print(tttxttt.replace("eldrian", "eldrian"))


