# Recursion method practice

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print (listsum([1,3,5,7,9]))

def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0] + numList[1:]

from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral (myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)
drawSpiral(myTurtle,100)
myWin.exitonclick()