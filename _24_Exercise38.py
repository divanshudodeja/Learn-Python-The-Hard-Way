ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10things in that list")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)
    print("There are %d items now" % len(stuff))

print("There we go", stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))