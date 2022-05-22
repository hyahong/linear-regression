import csv
from inspect import _void
from estimate import estimatePrice

# total sum of squares
def sst(prices):
    result = 0.0
    avg = sum(prices) / len(prices) 
    for price in prices:
        result += (price - avg) ** 2
    return result

# residual sum of squares
def ssr(t0, t1, mileages, prices, param):
    result = 0.0
    avg = sum(prices) / len(prices) 
    for mileage, price in zip(mileages, prices):
        result += (estimatePrice(t0, t1, mileage, param) - avg) ** 2
    return result

def main():
    t0, t1 = [0.0, 0.0]
    mileages = []
    prices = []
    # theta
    with open('thetas.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            t0 = float(row[0])
            t1 = float(row[1])
            break
    # file
    with open('data.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if (row[0] != 'km'):
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
    # param
    param = [max(mileages), min(mileages), max(prices), min(prices)]
    print('accuracy:', ssr(t0, t1, mileages, prices, param) / sst(prices))

if __name__ == "__main__":
    main()