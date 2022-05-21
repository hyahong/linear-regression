import csv

def estimatePrice(t0, t1, mileage, maxMileage, minMileage, maxPrices, minPrices):
    normailzed = t0 + t1 * (mileage - minMileage) / (maxMileage - minMileage)
    return normailzed * (maxPrices - minPrices) + minPrices 

def main():
    t0, t1 = [0.0, 0.0]
    mileages = []
    prices = []

    with open('thetas.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            t0 = float(row[0])
            t1 = float(row[1])
            break

    with open('data.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if (row[0] != 'km'):
                mileages.append(float(row[0]))
                prices.append(float(row[1]))

    while 1:
        try:
            mileage = float(input("mileage: "))
            if (mileage >= 0):
                break
            print("invalid input.")
        except:
            print("invalid input.")
    print("estimated price:", estimatePrice(t0, t1, mileage, max(mileages), min(mileages), max(prices), min(prices)))

if __name__ == '__main__':
    main()