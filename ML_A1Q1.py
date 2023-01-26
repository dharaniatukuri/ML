ages = [19,22,19,24,20,25,26,24,25,24]
#sorting the list and assigning the min and max age
ages.sort()
minage = min(ages)
maxage = max(ages)
#Adding the min age and the max age to the ages
ages.append(minage)
ages.append(maxage)
ages.sort()
#Calculating the median age
length = len(ages)
medianAge = ages[ (length+1)//2] if length%2==1 else (ages[length//2]+ages[ (length//2)+1])/2
#Calculating the average ages and the range of the ages
sumofAges = sum(ages)
averageofAges = sumofAges//length
rangeofAges = maxage-minage
#printing all the values
print(minage)
print(maxage)
print(medianAge)
print(averageofAges)
print(rangeofAges)
