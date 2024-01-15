# required to represent the digit i
import math
sticks = [6, 2, 5, 5, 4, 5,
          6, 3, 7, 6]


# Function to return the count of
# matchsticks required to represent  
# the given number  
def countSticks(string, n):
    cnt = 0

    # For every digit of the given number  
    for i in range(n):
        # Add the count of sticks required
        # to represent the current digit  
        cnt += (sticks[ord(string[i]) - ord('0')])

    return cnt


# Driver code
if __name__ == "__main__":


    for i in range(0,25):
        print(i)
        print(i, math.ceil(i/7))
        print(i, math.floor(i/2), "fl")
        print(i, i//2, "//")
        print(i, i/2, "/")


    # This code is contributed by AnkitRai01
