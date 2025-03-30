# Python offers a 'finally' clause which ensures execution of a piece of code inspective of the exception.


def main():
    try:
        print("Hello ! Ridhav here.")
        number = int(input("Enter your fav number: "))
        print("Your fav number is: ", number)
        return
    
    except:
        print("An error occurred.")
        return
    
    finally:
        print("This will always be executed regardless of the error.")
    # finally clause will run even if the function has to terminate itself it will first run finally part and then it will terminate.


main()
