import pandas



def addDataDist(dataDist, chunkSize, file):
    csv_reader = pd.read_csv(file, chunkSize=chunkSize)

    for i, chunk in enumarate(csv_reader):
        if i == 3:
            for i in chunk[3]:
                if i == "label_id":
                    continue
                if i not in dataDist:
                    dataDist[i] = 0
                else:
                    dataDist[i] += 1
    return dataDist

dataDist = {}
dataDist = addDataDist(dataDist,600,"femnist.csv")

keys = list(dataDist.keys())
values = list(dataDist.values())

plt.bar(keys, values)

plt.xlabel('Data')
plt.ylabel('Occurrence')
plt.title('Data distribution of femnist')

plt.savefig('dist_femnist.png')