import pandas as pd
import time
from alpha_vantage.timeseries import TimeSeries

api_key = '54YXAP093L7O9I8T'


dataraw = TimeSeries(key=api_key, output_format='pandas')

data, meta_data = dataraw.get_intraday(symbol='TSLA', interval='1min', outputsize= 'full')

print(data)



