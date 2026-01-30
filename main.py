from sum import add_numbers
from difference import subtract_numbers

def main():
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))


    total = add_numbers(a, b)
    diff = subtract_numbers(a, b)

    
    print("Sum is:", total)
    print("Difference is:", diff)


if __name__ == "__main__":
    main()
