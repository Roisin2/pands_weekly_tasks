'''Program called collatz.py, that asks u to input any positive int and outputs the successive values of the following
 At each step cal the next val by taking the current val, if even, divide it by 2, but if odd, multiply it by three
and add one.End if the c print
'''
#Author:Roisin Stanley

print("This is The Collatz Sequence")

def collatz(number):
    sequence = [number]
    # Generates the successive values of the Collatz sequence for a given positive integer.
    
    
    while number != 1:  # continue till sequence = 1
        if number % 2 == 0: # if number is even
            number = number // 2  # divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1
            sequence.append(number) # add new number to sequence
    return sequence  

def main():
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            print("Please enter a positive integer.")           # ask again if number but not poisitive int
            return
        sequence = collatz(number)
        print(f"sucessive values of sequence: {sequence}")      # is positive int print output of function
    except ValueError:
         print("Invalid input. Please enter a positive integer.")   # err for non number inputs

if __name__ == "__main__":
    main()


# reference: https://codereview.stackexchange.com/questions/256054/basic-collatz-program-with-input-validation-in-pytho