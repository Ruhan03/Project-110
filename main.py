import statistics as st
import pandas  as pd
import random as rd
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
population_mean = st.mean(data)
print('The Mean of the Whole Population of Reading Time is: ',str(population_mean))

def getMean():
    list = []
    for i in range(0, 30):
        rdIndex= rd.randint(0,len(data)-1)
        value = data[rdIndex]
        list.append(value)
    mean = st.mean(list)
    return mean

def plotGraph(list):
    fig = ff.create_distplot([list],['Reading Time'],show_hist=False,colors=['#22628e'])
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        mean = getMean()
        meanList.append(mean)
    finalMean = st.mean(meanList)
    print('The Mean of the Sampling Data is: ',finalMean)
    plotGraph(meanList)

setup()

