def Isfibonacci(n):
    x, y = 0, 1
    while x < n:
        x, y = y, x + y
    return x == n

def main():
    list = []
    
    while True:
        num_input = input("ENTER A NUMBER : ")
        
        if num_input.startswith('-') and num_input[1:].isdigit():
            break
        elif num_input.isdigit():
            num = int(num_input)
            list.append(num)
        else:
            print("INVALID NUMBER! PLEASE ENTER THE CORRET NUMBER")

    fibonacci_numbers = [num for num in list if Isfibonacci(num)]

    print("\nTOTAL NUMBER OF FIBONACII NUMBER", len(fibonacci_numbers))
    if len(fibonacci_numbers) == 0:
        print("\nERROR: NO FIBONACCI NUMBER IS FOUND")

if __name__ == "__main__":
    main()
