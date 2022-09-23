from numpy import sort

## print a function ##
#print("hello Mom!!")

#list1 = [1,1,2,4,8,96,5,444,00]
#print("Given list is " )
#print(list1)
#print(" an the sorted list is ")
#list1.sort()
#print(list1)

## creating a dictionary {} ##
dict  = {"name":"awaiz","age":32,"city":"vattepally","status":"single"}
dict["height"] = 7.0
#print(dict['status'])

## if else ##
# if (3>20):  
    # print('hello mother')
# elif 3==3:
    # print('equals to')
# else:
    # print('condition false')

# defining functions ##
#def add(name):
#    if name == 'danish':
#        print('aree goli lagaya danis lo')
#        print('hum theek hai abba..... hum theek hai')
#    elif name == 'owaiz':
#        print('lays bhi laye kya')
#    else:
#        print(name)
#add('manoj')

for name,value in dict.items():
    if (value == 'awaiz'):
        print('hello' + value)