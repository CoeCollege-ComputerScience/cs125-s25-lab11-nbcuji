blue = set("abcdijklm")
red = set("defghijnop")
green = set("ijklmnopqrst")

intersection_set = blue.intersection(set(red), set(green))
print(intersection_set)

difference = blue.difference(red, green)
print(difference)

anotherintersection = red.intersection(green)
print(anotherintersection)

purple = blue.intersection(red).difference(green)
print(purple)

brown = green.intersection(red)
bluegreen = green.intersection(blue)
themiddleofthevenndiagram = brown.intersection(bluegreen)
result = (brown.union(bluegreen)).difference(themiddleofthevenndiagram)
print(result)