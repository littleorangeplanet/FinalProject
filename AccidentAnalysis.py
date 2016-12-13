import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class AccidentAnalysis:

	
	def __init__(self, df):
		self.df = df
		self.df['YEAR'] = [x[6:] for x in self.df['DATE']]
		self.df['MONTH'] = [x[:2] for x in self.df['DATE']]		

	def stats_borough(self, borough):
		''' get the number of accidents of specific borough '''
		df_borough = self.df.loc[self.df['BOROUGH'] == borough.upper()]
		return df_borough

	def stats_year(self, year):
		''' get the number of accidents of specific year '''

		df_year = self.df.loc[self.df['YEAR'] == year]
		return df_year

	def stats_month(self, month):
		''' get the number of accidents of specific year '''

		df_month = self.df.loc[self.df['MONTH'] == month]
		return df_month

	def stats_loc(self, loc):
		''' get the number of accidents of specific location '''
		
	def stats_loc(self, reason):
		''' get the number of accidents of specific reason '''
	
	def stats_loc(self, type):
		''' get the number of accidents of specific vehicle type '''

	def borough_year_count(self, borough = "ALL", type = "None"):
		''' show the change of total accident counts of particular borough over the years '''
		fig = plt.figure()
		fig.clear()
		if borough != "ALL":
			''' when borough is defined, show the line plot of that chosen borough '''
			df_borough = self.df.loc[self.df['BOROUGH'] == borough]#.upper()]
			df_borough_year_count = df_borough.groupby(['YEAR'])['YEAR'].count()
			df_borough_year_count.plot()
			plt.xlabel('Numbers of Collisions')
			plt.ylabel('Years')
			plt.grid()
			plt.title('The Number of Collisions for %s' %  borough.upper())
			# plt.show()

		else:
			''' when no borough is defined, show the line plot of all borough '''
			boro_year_ser = self.df.groupby(["BOROUGH", 'YEAR'])['UNIQUE KEY'].count()
			boro_year = boro_year_ser.to_frame()
			boro_year = boro_year.rename(columns = {'UNIQUE KEY':'Counts'})

			
			plt.plot(boro_year.xs('BRONX', level=0))
			plt.plot(boro_year.xs('BROOKLYN', level=0))
			plt.plot(boro_year.xs('MANHATTAN', level=0))
			plt.plot(boro_year.xs('QUEENS', level=0))
			plt.plot(boro_year.xs('STATEN ISLAND', level=0))

			plt.xlabel('Numbers of Collisions')
			plt.ylabel('Years')
			plt.grid()
			plt.title('The Number of Collisions for All Boroughs')
			plt.legend(['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND'], loc='upper left')
			# plt.show()
		
		return fig


def obj():
	filename = "NYPD_Motor_Vehicle_Collisions.csv"
	df = pd.read_csv(filename)
	df_1 = df.replace(['Unspecified'], np.nan)
	obj = AccidentAnalysis(df_1)

	return obj


