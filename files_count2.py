#import files from library
import sys

f = open('MyPythonNotes.txt', 'r' )
lines = f.readlines()
f.close()
print('The contents of the file is:')
for line in lines:
    print(line)

f = open('MyPythonNotes.txt', 'a' )
count = 11
#requesting user for 11th python interesting fact
print("Enter the 11th intresting fact about Python (should be a complete sentence format)")
facts = input(str(count)+': ')
f.write(str(count)+': '+facts+'\n')
f.close()

f = open('MyPythonNotes.txt', 'r' )
lines = f.readlines()
f.close()
print('The current contents of the file is:')
for line in lines:
    print(line)
