import pandas as pd
import numpy as np
from AccidentAnalysis import *
import matplotlib.pyplot as plt

filename = "NYPD_Motor_Vehicle_Collisions.csv"
df = pd.read_csv(filename)
df_1 = df.replace(['Unspecified'], np.nan)
# print(df_1)

a = AccidentAnalysis(df_1)
# queens = a.stats_borough('queens')
# print(queens)

# year_2016 = a.stats_year('2016')
# print(year_2016)

# month_06 = a.stats_month('06')
# print(month_06)


a.borough_year_count(borough = 'queens')

