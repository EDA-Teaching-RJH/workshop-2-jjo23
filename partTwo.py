import math  

def main():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    pythag(num1, num2)

def pythag(A,B):
    sqr = A**2 + B**2
    root = math.sqrt(sqr)
    print(f"the length of the hyp is {root}")

main()

