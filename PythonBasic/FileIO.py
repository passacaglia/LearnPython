spath="D:/temp/test.txt"
f=open(spath,"w") # Opens file for writing.Creates this file doesn't exist.
f.write("First line 1.\n")
f.writelines("First line 2.")

f.close()

f=open(spath,"r") # Opens file for reading

for line in f:
    print line
f.close()
