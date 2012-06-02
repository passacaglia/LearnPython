print "I am 6'2\" tall." # escape double-quote inside string
print 'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

lovely_cat = "Hello, Kitty, %r"
nice = 'little ball of fur'

soft_kitty = """
Soft kitty, warm kitty,\n%s.
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print lovely_cat % (nice)
print soft_kitty % (nice)
