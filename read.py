"""f= open("one.txt","r")
data=f.read(10)
print("first part:",data)
f.close()"""

"""f= open("one.txt","r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)
f.close()"""


"""f=open("one.txt","r")
lines=f.readline()
print("List of lines: ",lines)
print("Number of lines: ",len(lines))
f.close()"""

"""f=open("one.txt")
data=f.read()
print("file content:",data)
f.close()"""

f=open("one.txt","r")
lines=f.readlines()
print(lines[3].strip())
f.close()
