import sys
prog = sys.argv[0]
file = sys.argv[1]
print("filename = {}".format(file))

with open(file) as f:
    for line in f:
        print(line.rstrip())
        fields = line.split()
        print("fields[0] {}, fields[1] {}".format(fields[0], fields[1]))