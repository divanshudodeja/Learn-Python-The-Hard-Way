from sys import argv

script, filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit return.")

input("?")

print("Opening file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("Going to write these lines to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And then we close it")

target.close()