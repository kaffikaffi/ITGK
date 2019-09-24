def testingFunctions(temp):
    if temp <= 0:
        print("Kaldt vintervær")
    elif temp >= 1 and temp <= 9:
        print("Typisk trøndervær")
    elif temp >= 10:
        print("sommerVær")

testingFunctions(4)