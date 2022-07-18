# TASK

"""Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird"""

n = int(input(""))
if n >=1 and n <=100:
    if n % 2 == 0:
        if n in range(2,5):
            print("Not Weird")

        elif n in range(6,20):
            print("Wierd")

        elif n > 20:
            print("Not Weird")

    else:
        print("Weird")