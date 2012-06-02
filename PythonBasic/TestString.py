word = "abcdefg"
a = word[2]
print ("a is : " + a);
b = word[1:3]
print ("b is : " + b); # index 1 and 2 elements of word.
c = word[:2]
print ("c is : " + c); # index 0 and 1 elements of word.
d = word[0:]
print ("d is : " + d); # All elements of word.
e = word[:2]+word[2:]
print ("e is : " + e); # All elements of word.
f = word[-1]
print ("f is : " + f); # The last element of word.
g=word[-4:-2]
print "g is: "+g # index 3 and 4 elements of word.
h=word[-2:]
print "h is: "+h # The last two elements.
i=word[:-2]
print "i is: "+i # Everything except the last two characters
l=len(word)
print "Length of word is: "+ str(l)


#请注意ASCII和UNICODE字符串的区别
print "Input your Chinese name:"
s=raw_input("Press enter to be continued ");
print "Your name is   : " +s;
l=len(s)
print "Length of your Chinese name in asc codes is:"+str(l);
a=unicode(s,"GBK")
l=len(a)
print "I'm sorry we should use unicode char!Characters number of your Chinese \
name in unicode is:"+str(l);

