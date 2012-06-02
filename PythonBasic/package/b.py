# b.py
from a import add_func # Also can be : import a

print "Import add_func from module a"
print "Result of 1 plus 2 is: "
print add_func(1,2)    # If using "import a" , then here should be "a.add_func"
