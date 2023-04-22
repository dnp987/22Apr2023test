def function2(num, text):
    if (num > 5):
        print ("Number is too big")
        return False
    print ("number ", num , " is OK.")
    
    for step in range(num):
        print (step, " : ", text)
    return True