import os

import pandas as pd

import matplotlib.pyplot as plt

from influxdb_client import InfluxDBClient, WriteOptions

from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/jena_climate_2009_2016.csv")

df = df[['Date Time', 'T (degC)']]

df.index = pd.to_datetime(df.pop('Date Time'), format='%d.%m.%Y %H:%M:%S')

df['Measured Fluid'] = ['Air'] * df.shape[0]

plt.plot(df['T (degC)'])

plt.show()
