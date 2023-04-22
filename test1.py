if __name__ == "__main__":

    from datetime import datetime
    import re
    from tests.test2 import function1
    
    date_time = datetime.now().strftime('%Y %B %d %I %M %p') # get the date and time
    print (date_time)
    number = 10
    text = "This is a test"
    result = function1(number, text)
    if not result:
        print ("test failed")
    else:
        print ("test passed")