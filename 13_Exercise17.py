from sys import argv
from os.path import exists

#open(argv[2], 'w').write(open(argv[1]).read())

script, from_file, to_file = argv

print("Coping from %s to %s" %(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Doe the output file exists? %r" % exists(to_file))
print("Ready, hit Return to continue, CTRL^C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

