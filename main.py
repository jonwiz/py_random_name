from modules import RandomName


generate = RandomName.randomNames(needle="Jon", nameCount=3, charLen=3)

print(generate)


print("Generating Random Male Name:\n")
#try to generate firstname tim
print(RandomName.randomFullName('m'))

print("Generating Random Female Name:\n")
#try to generate firstname tim
print(RandomName.randomFullName('f'))