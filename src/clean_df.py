import pandas as pd
import numpy as np

class CleanDF(object):
	def __init__(self):
		self.df = pd.DataFrame()
	
	def left_merge(self, other, on='SEQN'):
		self.df = self.df.merge(other.df, how='left', on=on)

class DemographicDF(CleanDF):
	def __init__(self):
		self.df = pd.read_csv('../data/demographic.csv')[['SEQN','RIAGENDR','RIDAGEYR','RIDRETH3',
															'DMQMILIZ','DMQADFC','DMDBORN4','DMDMARTL']]
		self.column_dict = {
			'RIAGENDR': {1.0: 'Male', 2.0: 'Female', '.': np.nan},
			'RIDRETH3': {1.0: 'Mexican American',
						 2.0: 'Other Hispanic',
						 3.0: 'White',
						 4.0: 'Black',
						 6.0: 'Asian',
						 7.0: 'Other Race (or Multi-Racial',
						 '.': np.nan
						},
			'DMQMILIZ': {1.0: 'Yes',2.0: 'No',7.0: np.nan,9.0: np.nan,'.': np.nan},
			'DMQADFC': {1.0: 'Yes',2.0: 'No',7.0: np.nan,9.0: np.nan,'.': np.nan},
			'DMDBORN4': {1.0: 'Born in US',2.0: 'Others',77.0: np.nan,99.0: np.nan,'.': np.nan},
			'DMDMARTL': {1.0: 'Married',2.0: 'Widowed',3.0: 'Divorced',4.0: 'Separated',5.0: 'Never married',6.0: 'Living w/ partner',77.0: np.nan,99.0: np.nan,'.': np.nan}
		}
		self.clean_data()


	def clean_data(self):
		self.df = self.df.fillna(value='.')
		def make_readable(self, column, x):
			return self.column_dict[column][x]
		for column in self.df.columns:
			if column in self.column_dict:
				self.df[column] = self.df[column].apply(lambda x: make_readable(self,column,x))

class ExamDF(CleanDF):
	def __init__(self):
		super(ExamDF,self).__init__()
		self.df = pd.read_csv('../data/examination.csv')[['SEQN','BPXSY1','BPXSY2','BPXSY3','BPXSY4','BPXDI1','BPXDI2','BPXDI3','BPXDI4']]
		self.create_average_bp_columns()
		self.drop_other_columns()
	
	def create_average_bp_columns(self):
		self.df['AVG SYS BP'] = self.df[['BPXSY1','BPXSY2','BPXSY3','BPXSY4']].mean(axis=1)
		self.df['AVG DIAS BP'] = self.df[['BPXDI1','BPXDI2','BPXDI3','BPXDI4']].mean(axis=1)
		self.df['High SYS BP?'] = self.df['AVG SYS BP'].apply(lambda x: x >= 130)
		self.df['High DIAS BP?'] = self.df['AVG DIAS BP'].apply(lambda x: x >= 80)
	
	def drop_other_columns(self):
		self.df = self.df.drop(['BPXSY1','BPXSY2','BPXSY3','BPXSY4','BPXDI1','BPXDI2','BPXDI3','BPXDI4'],axis=1)

class LabsDF(CleanDF):
	def __init__(self):
		super(LabsDF,self).__init__()
		self.df = pd.read_csv('../data/labs.csv')[['SEQN','LBXHCT','LBXTR']]

class QuestDF(CleanDF):
	def __init__(self):
		super(QuestDF,self).__init__()
		self.df = pd.read_csv('../data/questionnaire.csv')[['SEQN','BPQ020','BPQ080','BPQ040A','BPQ050A','BPQ090D']]
		self.entry_dict = {1.0: 'Yes', 2.0: 'No', 7.0: np.nan, 9.0: np.nan, '.': np.nan}
		self.clean_data()
	
	def clean_data(self):
		self.df = self.df.fillna(value='.')
		def make_readable(self, x):
			try:
				return self.entry_dict[x]
			except KeyError:
				return x
		for column in self.df.columns:
			self.df[column] = self.df[column].apply(lambda x: make_readable(self,x))
	
if __name__ == '__main__':
	demo_df = DemographicDF()
	exam_df = ExamDF()
	ques_df = QuestDF()