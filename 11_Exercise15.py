from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r: " % filename)
print(txt.read())

print("Type the filename again:")
fie_again = input('> ')

txt_again = open(fie_again)

print(txt_again.read())