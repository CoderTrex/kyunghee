# #! /usr/bin/env python
from alphavantage import AlphaVantage
from timeseries import TimeSeries
from techindicators import TechIndicators
from sectorperformance import SectorPerformances
from foreignexchange import ForeignExchange
from fundamentaldata import FundamentalData
import matplotlib
import matplotlib.pyplot as plt
import os


# matplotlib.rcParams['figure.figsize']  = (20.0, 10.0)

# ts = TimeSeries(key=os.environ['API_KEY'], output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
# data.describe()


ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()