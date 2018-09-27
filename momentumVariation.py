#!/usr/bin/python

import fix_yahoo_finance as yf
yf.pdr_override()

import datetime
import dateutil
import matplotlib.pylab as plt

def calcMomentum(stockTicker,startDate,totalDays):
   # get 3 years ago
   last_day = startDate + dateutil.relativedelta.relativedelta(days=-totalDays)
   first_day  = last_day + dateutil.relativedelta.relativedelta(months=-36)

   # request the data from yahoo 
   stockData = yf.download(stockTicker, start=first_day, end=last_day)

   momentumScore = {}

   for n in range(totalDays):
      calcDate = startDate + dateutil.relativedelta.relativedelta(days=-n)
 
      month_1 = calcDate + dateutil.relativedelta.relativedelta(months=-1)
      month_3 = calcDate + dateutil.relativedelta.relativedelta(months=-3)
      month_6 = calcDate + dateutil.relativedelta.relativedelta(months=-6)
      month_12 = calcDate + dateutil.relativedelta.relativedelta(months=-12)
   
   
      stockDates = stockData.index
      closeCurrDay = stockData.ix[stockDates[-1]]['Adj Close']
   
      ## get Year to Date performance
      closestDate = min(stockDates,key=lambda date : abs(first_day-date))
      closeFirstDay = stockData.ix[closestDate]['Adj Close']
      perf_YTD =  (closeCurrDay - closeFirstDay)/closeFirstDay*100
   
      # Find closest day 1 month ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_1-date))
      closeValue_month_1 = stockData.ix[closestDate]['Adj Close']
      perf_1_month =  (closeCurrDay - closeValue_month_1)/closeValue_month_1*100
   
      # Find closest day 3 months ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_3-date))
      closeValue_month_3 = stockData.ix[closestDate]['Adj Close']
      perf_3_month =  (closeCurrDay - closeValue_month_3)/closeValue_month_3*100
      # Find closest day 6 months ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_6-date))
      closeValue_month_6 = stockData.ix[closestDate]['Adj Close']
      perf_6_month =  (closeCurrDay - closeValue_month_6)/closeValue_month_6*100
      # Find closest day 12 months ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_12-date))
      closeValue_month_12 = stockData.ix[closestDate]['Adj Close']
      perf_12_month =  (closeCurrDay - closeValue_month_12)/closeValue_month_12*100
   
      momentumScore[n] = perf_1_month + perf_3_month + perf_6_month + perf_12_month

   return momentumScore


if __name__ == "__main__":
    startDate = datetime.datetime.today()
    stockTicker = 'DFCIX'
    totalDays = 200
    momentum = calcMomentum(stockTicker,startDate,totalDays)

    lists = sorted(momentum.items())

    x, y = zip(*lists) # unpack a list of pairs into two tuples
    
    plt.plot(x, y)
    plt.show()
