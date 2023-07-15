import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


for arg in sys.argv[1:]:
    print("hello, my name is", arg)



# in terminal window type python3 /filepath [name]