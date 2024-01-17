file = open('2023_day_1.txt', 'r')
lines = file.readlines()

# strip out any non-int
cleaned = []

for l in lines:
    nums = "".join([e for e in l if e.isdigit()])
    cleaned.append(nums)

print(len(cleaned))

fnl = []

# strip out the first and last int
for l in cleaned:
    if len(l) <= 1:
        linesum = l+l
        fnl.append( int(linesum) )
    else:
        linesum = l[0]+l[-1]
        # print(linesum)
        fnl.append( int(linesum) )

print(len(fnl))
print(sum(fnl))

# sum each line
# sum all lines
# print the final sum
file.close()