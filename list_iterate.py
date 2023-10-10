ages = [33,56,32,64,63]
total = 0
for age in ages:
    total += age
 
print(total)

ages2 = ages

print(ages2)

ages[1] = 90
print(ages[1])
print(ages2[1])