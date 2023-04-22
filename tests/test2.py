def function1(num, text):
    if (num < 2):
        print ("Number is too small")
        return False
    print ("number ", num , " is OK.")
    
    for step in range(num):
        print (step, " : ", text)
    return True