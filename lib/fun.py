myList =[1,2,3,4]
print(myList[1])
myList=[7,6,3,9,2,1,4,5,8,10]
myList.sort()
print(myList)

myList=['apple','cabbage','banana']
myList.sort()
print(myList)

myList=['i am good',"cat"]
myList.sort(key= len )
print(myList)

myList=[('john',2),('cate',1)]
def sortTuple(tupleValue):
    return tupleValue[1]

myList.sort(key = sortTuple)
print(myList)

myList=[0,1,2,3,4,6]
myList.clear()
print(myList)

for n in range (2,6):
    print(n)

    myRange=range(5)
    print(myRange)


    myString='hello world'
   # for char in myString:
    myString=myString.upper()
    print(myString)