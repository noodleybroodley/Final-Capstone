import pandas as pd

class DemographicDF(object):

	def __init__(self):
		self.df = pd.read_csv('../data/demographic.csv')[['SEQN','RIAGENDR','RIDAGEYR','RIDRETH3',
'DMQMILIZ','DMQADFC','DMDBORN4','DMDMARTL']]
		self.column_dict = {
			'RIAGENDR': {1.0: 'Male', 2.0: 'Female'},
			'RIDRETH3': {1.0: 'Mexican American',
						 2.0: 'Other Hispanic',
						 3.0: 'Non-Hispanic White',
						 4.0: 'Non-Hispanic Black',
						 6.0: 'Non-Hispanic Asian',
						 7.0: 'Other Race (or Multi-Racial'
						},
			'DMQMILIZ': {1.0: 'Yes',2.0: 'No',7.0: 'Refused',9.0: "Don't Know",'.': 'Missing'},
			'DMQADFC': {1.0: 'Yes',2.0: 'No',7.0: 'Refused',9.0: "Don't Know",'.': 'Missing'},
			'DMDBORN4': {1.0: 'Born in US',2.0: 'Others',77.0: 'Refused',99.0: "Don't Know",'.': 'Missing'},
			'DMDMARTL': {1.0: 'Married',2.0: 'Widowed',3.0: 'Divorced',4.0: 'Separated',5.0: 'Never married',6.0: 'Living w/ partner',77.0: 'Refused',99.0: "Don't Know",'.': 'Missing'}
		}
		self.clean_columns()
	
	def change_entry_value()
	
	def clean_columns(self):
		for column in self.df.columns:
			#print(column)
			if column in self.column_dict:
				self.df[column] = self.df[column].apply(lambda x: self.column_dict[column][x])
				#self.df = self.df.drop(column)
				#self.df[column] = new_series

if __name__ == '__main__':
	demo_df = DemographicDF()
	demo_df.df.head(10)