import investpy
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import os as os
import glob as gl

data = investpy.get_stock_historical_data(stock='0001', 
                                            country='Hong Kong', 
                                            from_date='01/01/2020', 
                                            to_date='31/12/2020', 
                                            interval='daily')
print(data)

data.to_excel('0001.xlsx')
