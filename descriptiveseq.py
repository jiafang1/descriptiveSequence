#2 bonus questions are included in this code
#it is able to provide the correct answer for any iterations and any starting number
currentnum = input("Enter an integer as first entry: ")
numentry = input("Enter the number of entries: ")
try:
    currentnum = int(currentnum)
    numentry = int(numentry)
except ValueError:
   print("Error: one of your inputs was not an integer.")

#loop through number of elements
for n in range(numentry):
    #counter for each number
    numcount = ([],[])
    nextnum = ''
    prev = 999

    #loop through number of digits in each element
    for digit in str(currentnum):
        if prev == 999:
            numcount[0].append(digit)
            numcount[1].append(1)
        elif digit == prev:
            numcount[1][-1] += 1
        elif digit != prev:
            numcount[0].append(digit)
            numcount[1].append(1)
        prev = digit
    i = 0

    #collapse numcount into workable number within the sequence
    while i < len(numcount[0]):
        nextnum += str(numcount[1][i])
        nextnum += str(numcount[0][i])
        i += 1
    currentnum = int(nextnum)
    print (currentnum)

print ("Your result is: "+str(currentnum))

