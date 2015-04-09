#Returns the sum of num1 and num2. 
#function signature
def add(num1, num2):
    return num1 + num2

#Returns the difference of num1 and num2
def sub(num1, num2):
        return num1 - num2

#Returns the product of num1 and num2
def multiplication(num1, num2):
    return num1 * num2

#Returns the division of num1 and num2
def division(num1, num2):
    return num1 / num2



def main():
    #counter so does operation five times
    count = 0
    while(count < 5):
        operation = input("What do you want to do (+, -, *, /)")
        if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
            #invalid operation
            print("incorrect sign")
        else:
            num1 = int(input("Enter num1: "))
            num2 = int(input("Enter num2: "))
            if(operation == '+'):
                print(add(num1, num2))
            elif(operation == '-'):
                print(sub(num1, num2))
            elif(operation == '*'):
                print(multiplication(num1, num2))
            elif(operation == '/'):
                print(division(num1, num2))
            count = count + 1
        
main()