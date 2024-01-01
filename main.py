import csv
from matplotlib import pyplot as plt

dataDict = {}
computedCoeffs = []
computedCoeffsRefined = []
quarters = []
outlierMin = 50

GDPC1_CSV = "Revised_GDPC1.csv"
UNRATE_CSV = "Revised_UNRATE.csv"
NROU_CSV = "Revised_NROU.csv"
GDPPOT_CSV = "Revised_GDPPOT.csv"

csvList = [GDPC1_CSV, UNRATE_CSV, NROU_CSV, GDPPOT_CSV]

for i in range(0, 288):
    shift = i * 0.25
    date = 1949 + shift
    quarters.append(date)
    dataDict.update({date : []})

for file in csvList:
    values = []
    with open(file, 'r') as csvFile:
        # iterate through each line
        csvReader = csv.reader(csvFile)

        # skip the first row
        firstRow = next(csvReader)
        
        for row in csvReader:
            values.append(row[1])

    for i in range(0, 288):
        shift = i * 0.25
        date = 1949 + shift

        # add to current list of values
        currentList = dataDict[date]
        currentList.append(float(values[i]))
        dataDict.update({date : currentList})
        
for i in range(0, 288):
    shift = i * 0.25
    date = 1949 + shift

    a = dataDict[date][0]
    b = dataDict[date][1]
    c = dataDict[date][2]
    d = dataDict[date][3]

    # computes accurate okun's constant
    computedCoeffs.append(((d - a) / d) * 100 / (b - c))
    print("Date: " + str(date) + " Coeff: " + str(((d - a) / d) * 100 / (b - c)))

# graph with outliers
plt.plot(quarters, computedCoeffs)
#plt.show()

sumNoOuts = 0.0
outliers = 0.0

for x in computedCoeffs:    
    if abs(x) > outlierMin:
        outliers += 1.0
        computedCoeffsRefined.append(0.0)
    else:
        sumNoOuts += x
        computedCoeffsRefined.append(x)

# graph without outliers
plt.plot(quarters, computedCoeffsRefined)
plt.show()
print(outliers)
print(sumNoOuts / (len(quarters) - outliers))
    
