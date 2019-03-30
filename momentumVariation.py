#!/usr/bin/python

import fix_yahoo_finance as yf
yf.pdr_override()

import datetime
import dateutil
import matplotlib.pylab as plt


def smi_momentum(stock_ticker,final_day):
   print('Ticker\tEnd Date\t\t1 Mo\t3 Mo\t6 Mo\t12 Mo\tMom')

   for currentTicker in stock_ticker:
     first_day  = final_day + dateutil.relativedelta.relativedelta(months=-12)        
     
     month_1 = final_day + dateutil.relativedelta.relativedelta(months=-1)
     month_3 = final_day + dateutil.relativedelta.relativedelta(months=-3)
     month_6 = final_day + dateutil.relativedelta.relativedelta(months=-6)
     month_12 = final_day + dateutil.relativedelta.relativedelta(months=-12)
  
     # request the data from yahoo 
     stock_data = yf.download(currentTicker, start=first_day, end=final_day,progress=False)
     
     stock_dates = stock_data.index
     close_curr_day = stock_data.loc[stock_dates[-1]]['Adj Close']
     
     # Find closest day 1 month ago and calculate performance
     closest_date = min(stock_dates,key=lambda date : abs(month_1-date))
     close_value_month_1 = stock_data.loc[closest_date]['Adj Close']
     perf_1_month =  (close_curr_day - close_value_month_1)/close_value_month_1*100
     
     # Find closest day 3 months ago and calculate performance
     closest_date = min(stock_dates,key=lambda date : abs(month_3-date))
     close_value_month_3 = stock_data.loc[closest_date]['Adj Close']
     perf_3_month =  (close_curr_day - close_value_month_3)/close_value_month_3*100
  
     # Find closest day 6 months ago and calculate performance
     closest_date = min(stock_dates,key=lambda date : abs(month_6-date))
     close_value_month_6 = stock_data.loc[closest_date]['Adj Close']
     perf_6_month =  (close_curr_day - close_value_month_6)/close_value_month_6*100
  
     # Find closest day 12 months ago and calculate performance
     closest_date = min(stock_dates,key=lambda date : abs(month_12-date))
     close_value_month_12 = stock_data.loc[closest_date]['Adj Close']
     perf_12_month =  (close_curr_day - close_value_month_12)/close_value_month_12*100
  
     smi_momentum = perf_1_month + perf_3_month + perf_6_month + perf_12_month
  
  # =============================================================================
     print('%s\t%s\t%2.2f\t%2.2f\t%2.2f\t%2.2f\t%2.2f' 
        %(currentTicker,\
          final_day.strftime("%B %d, %Y"),perf_1_month,\
          perf_3_month,perf_6_month,\
          perf_12_month, smi_momentum))
  # =============================================================================
  
  #   print '%s  %s  %2.1f' %(currentTicker,\
  #                           final_day.strftime("%B %d, %Y"),smi_momentum)
     
   return smi_momentum

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
      closeCurrDay = stockData.loc[stockDates[-1]]['Adj Close']
   
      ## get Year to Date performance
      closestDate = min(stockDates,key=lambda date : abs(first_day-date))
      closeFirstDay = stockData.loc[closestDate]['Adj Close']
      perf_YTD =  (closeCurrDay - closeFirstDay)/closeFirstDay*100
   
      # Find closest day 1 month ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_1-date))
      closeValue_month_1 = stockData.loc[closestDate]['Adj Close']
      perf_1_month =  (closeCurrDay - closeValue_month_1)/closeValue_month_1*100
   
      # Find closest day 3 months ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_3-date))
      closeValue_month_3 = stockData.loc[closestDate]['Adj Close']
      perf_3_month =  (closeCurrDay - closeValue_month_3)/closeValue_month_3*100
      # Find closest day 6 months ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_6-date))
      closeValue_month_6 = stockData.loc[closestDate]['Adj Close']
      perf_6_month =  (closeCurrDay - closeValue_month_6)/closeValue_month_6*100
      # Find closest day 12 months ago and calculate performance
      closestDate = min(stockDates,key=lambda date : abs(month_12-date))
      closeValue_month_12 = stockData.loc[closestDate]['Adj Close']
      perf_12_month =  (closeCurrDay - closeValue_month_12)/closeValue_month_12*100
   
      momentumScore[n] = perf_1_month + perf_3_month + perf_6_month + perf_12_month

   return momentumScore


if __name__ == "__main__":
    #startDate = datetime.datetime.today()
    #stockTicker = 'DFCIX'
    
    stock_ticker = [
      'GLFOX',
      'PID',
      ]
    final_day = datetime.datetime(2019,2,28,0,0,0,0)
    smi_momentum(stock_ticker,final_day)
    
    
# =============================================================================
#     totalDays = 200
#     momentum = calcMomentum(stockTicker,startDate,totalDays)
# 
#     lists = sorted(momentum.items())
# 
#     x, y = zip(*lists) # unpack a list of pairs into two tuples
#     
#     plt.plot(x, y)
#     plt.show()
# 
# =============================================================================
