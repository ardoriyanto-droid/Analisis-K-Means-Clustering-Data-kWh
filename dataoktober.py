import pandas as pd
import matplotlib.pyplot as plt

dfkwh = pd.read_csv('dataoktober.csv',sep=';',engine='python')
print(dfkwh.head())nonlocal