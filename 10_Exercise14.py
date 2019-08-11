from sys import argv

script, user_name = argv
prompt = '>'

print("Hi %s, I'm the %s script." %(user_name, script))

likes = input(prompt)

print("Where do you live %s" %user_name)
lives = input(prompt)