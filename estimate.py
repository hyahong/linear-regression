import csv

def estimatePrice(t0, t1, mileage, param):
    if t0 == 0 and t1 == 0:
        return 0
    normailzed = t0 + t1 * (mileage - param[1]) / (param[0] - param[1])
    return normailzed * (param[2] - param[3]) + param[3]

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
    param = [max(mileages), min(mileages), max(prices), min(prices)]
    print("estimated price:", estimatePrice(t0, t1, mileage, param))

if __name__ == '__main__':
    main()