# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = int(input("Enter a number: "))
#num = int(num)
def even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

even(num)
