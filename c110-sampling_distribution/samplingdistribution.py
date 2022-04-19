import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["readingtime"].tolist()
fig = ff.create_distplot([data], ["readingtime"], show_hist = False)
fig.show()

print("Population Mean: ", statistics.mean(data))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        randomindex = random.randint(0,len(data))
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ["readingtime"], show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(10)
        meanlist.append(set_of_means)
    show_fig(meanlist)
    print("Sampling Mean: ", statistics.mean(meanlist))
setup()
