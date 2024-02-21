#https://www.codewars.com/kata/57102bbfd860a3369300089c
from math import sqrt
def sensor_analysis(sensor_data):
    datas = [data[1] for data in sensor_data]

    mean = round(sum(datas) / len(sensor_data), 4)
    
    standard_deviation = sqrt(sum([(data-mean)**2 for data in datas]) / (len(sensor_data)-1))
    
    return mean, round(standard_deviation, 4)
  