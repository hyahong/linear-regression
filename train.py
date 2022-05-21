import matplotlib.pyplot as plt
import csv

def estimatePrice(t0, t1, mileage, param):
    normailzed = t0 + t1 * (mileage - param[1]) / (param[0] - param[1])
    return normailzed * (param[2] - param[3]) + param[3]

def lossFunction(t0, t1, mileages, prices):
    loss = 0.0
    for mileage, price in zip(mileages, prices):
        loss += (price - (t0 + t1 * mileage)) ** 2
    return loss / len(mileages)

def gradientDescent(t0, t1, learningRate, loss, mileages, prices):
    s0, s1 = [0.0, 0.0]
    for mileage, price in zip(mileages, prices):
        s0 += (t0 + t1 * mileage) - price
        s1 += ((t0 + t1 * mileage) - price) * mileage
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
    return t0, t1
 
def main():
    learningRate, epoch = [0.4, 1000]
    mileages = []
    prices = []
    # file
    with open('data.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if (row[0] != 'km'):
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
    # figure 1
    plt.figure(1)
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.scatter(mileages, prices, s=10, c='green')
    # param
    param = [max(mileages), min(mileages), max(prices), min(prices)]
    for i in range(0, len(mileages)):
        mileages[i] = (mileages[i] - param[1]) / (param[0] - param[1])
        prices[i] = (prices[i] - param[3]) / (param[2] - param[3])
    # train
    t0, t1 = train(learningRate, epoch, mileages, prices)
    # save result to file 'thetas.csv'
    with open("thetas.csv", 'w') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow([t0, t1])
    # draw
    plt.plot([param[1], param[0]], [estimatePrice(t0, t1, param[1], param), estimatePrice(t0, t1, param[0], param)], c='red')
    plt.show()

if __name__ == "__main__":
    main()