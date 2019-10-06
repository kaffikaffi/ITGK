def testingFunctions(temp):
    if temp <= 0:
        print("Kaldt vintervær")
    elif temp < 10:
        print("Typisk trøndervær")
    else: 
        print("sommervær")

degrees = int(input("Hvor mange greder er det? : "))

testingFunctions(degrees) 