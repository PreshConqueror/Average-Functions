#average function

#defining my_greatest function
def my_greatest(v1,v2,v3):
    #Calculating average of the three values that will be entered
    avg = int((v1+v2+v3/3))
    print('The average of the three numbers entered is:', avg)

#Requesting user to input three values
value1 = int(input('Enter first value: '))
value2 = int(input('Enter second value: '))
value3 = int(input('Enter third value: '))

my_greatest(value1, value2, value3)
