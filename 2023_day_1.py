# Advent of Code - Day 1 - Part 1

file = open('2023_day_1.txt', 'r')
lines = file.readlines()

# strip out any non-int
cleaned = []

for l in lines:
    nums = "".join([e for e in l if e.isdigit()])
    cleaned.append(nums)

# DEBUG CODE: print(len(cleaned))

# Grab the first and last number in each line

fnl = []

for l in cleaned:
    if len(l) <= 1:
        linesum = l+l
        fnl.append( int(linesum) ) # join the line and add
    else:
        linesum = l[0]+l[-1]
        fnl.append( int(linesum) ) #join the line and add


# DEBUG CODE: print(len(fnl)) # Verifies the correct amount of lines got read.

print(sum(fnl))

file.close()