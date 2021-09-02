#Program writing to files
#importing system files
import sys

f = open('MyPythonNotes.txt', 'a' )
count = 1
#Prompting user for ten interesting facts about Python
print("Enter ten intresting fact about Python (should be a complete sentence format)")
while count <= 10:
    facts = input(str(count)+': ')
    f.write(str(count)+': '+facts+'\n')
    count+=1

f.close()
print('Thank you, we have 10 facts')
f = open('MyPythonNotes.txt', 'r' )
lines = f.readlines()
f.close()
print('The contents of the file is:')
for line in lines:
    print(line)
