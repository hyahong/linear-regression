import csv

def estimatePrice(t0, t1, mileage):
    return t0 + t1 * mileage

def lossFunction(t0, t1, mileages, prices):
    loss = 0.0
    for mileage, price in zip(mileages, prices):
        loss += (price - estimatePrice(t0, t1, mileage)) ** 2
    return loss / len(mileages)

def gradientDescent(t0, t1, learningRate, loss, mileages, prices):
    s0, s1 = [0.0, 0.0]
    for mileage, price in zip(mileages, prices):
        s0 += estimatePrice(t0, t1, mileage) - price
        s1 += (estimatePrice(t0, t1, mileage) - price) * mileage
    if loss > lossFunction(t0 - learningRate * s0 / len(mileages), t1 - learningRate * s1 / len(mileages), mileages, prices):
        t0 -= learningRate * s0 / len(mileages)
        t1 -= learningRate * s1 / len(mileages)   
        loss = lossFunction(t0, t1, mileages, prices)
        learningRate *= 1.04
    else:
        learningRate *= 0.6
    return t0, t1, learningRate, loss

def train(learningRate, epoch, mileages, prices):
    t0, t1 = [0.0, 0.0]
    loss = lossFunction(t0, t1, mileages, prices)
    for _ in range(0, epoch):
        t0, t1, learningRate, loss = gradientDescent(t0, t1, learningRate, loss, mileages, prices) 
        print(t0, t1, learningRate)
    return t0, t1
 
def main():
    learningRate, epoch = [0.4, 1000]
    mileages = []
    prices = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if (row[0] != 'km'):
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
    t0, t1 = train(learningRate, epoch, mileages, prices)
    print(t0, t1)
    print(estimatePrice(t0, t1, 84000.0))

if __name__ == "__main__":
    main()