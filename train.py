import csv

def estimatePrice(t0, t1, mileage):
    return t0 + t1 * mileage

def train(t0, t1, learningRate, mileages, prices):
    size = len(mileages)
    s0, s1 = [0.0, 0.0]
    for i in range(0, size):
       s0 = (estimatePrice(t0, t1, mileages[i]) - prices[i])
       s1 = (estimatePrice(t0, t1, mileages[i]) - prices[i]) * mileages[i]
       t0 += learningRate * s0 / size
       t1 += learningRate * s1 / size
    return t0, t1
 
def main():
    t0, t1, learningRate = [0.0, 0.0, 0.5]
    mileages = []
    prices = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if (row[0] != 'km'):
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
    t0, t1 = train(t0, t1, learningRate, mileages, prices)
    print(t0, t1)

if __name__ == "__main__":
    main()