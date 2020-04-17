import numpy as numpy
k = int(input("Enter k (The sum to reach): "))
N = int(input("Enter N (amount of real numbers in the array): "))
B = int(input("Enter B (the range of the numbers will be in I[-B...0...B] ):"))
# Make sure b is positive
if (B < 0):
    B = -B
# Get array of random numbers.
# Add one to b so that we also get B in the array.
numbers = numpy.random.randint(low=-B, high=(B+1), size=N)
numbers = sorted(numbers)

positiveNumbers = list()
negativeNumbers = list()
for num in numbers:
    if num < 0:
        negativeNumbers.append(num)
    else:
        # Note we include zero to the positiveNumbers
        positiveNumbers.append(num)

# Add your own array here if you want to override the generated arrays.
positiveNumbers = sorted(positiveNumbers)
negativeNumbers = sorted(negativeNumbers, reverse=True)

print(positiveNumbers)
print(negativeNumbers)
# We now have our sorted list
# Start work on actualy algorithm

# Case that zero is not in the array (we are looking for 3 numbers that add up to 0)
# Idea is we get the smallest positive integer number (pn e0) (a), add the smallest negative number (nn e0) (b),
# and (if that is < k) then check the next positive number (e1).
# Also store the differenence of k - (sp + sn) if e1 is < diff, continue
# If e1 is == diff, output, if bigger, go back to a and continue
solution = False
for a in positiveNumbers:
    continueA = False
    finished = False
    for b in negativeNumbers:
        if (a + b >= k):
            continue
        diff = k - (a + b)
        # TODO: Think of a better solution than this boolean, maybe a .remove or something.
        skippedA = False
        for c in positiveNumbers:
            if (c == a and not skippedA):
                skippedA = True
                continue
            if (c < diff):
                continue
            elif (c == diff):
                print("Solution: " + str(a) + " + " +
                      str(b) + " + " + str(c) + " = " + str(k))
                finished = True
                solution = True
                break
            else:
                continueA = True
                break
        if (finished or continueA):
            break
    if (continueA):
        continue
    if (finished):
        break
if not solution:
    print("Could not find a solution using the given array.")