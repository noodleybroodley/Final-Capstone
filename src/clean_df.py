import pandas as pd
import numpy as np

class CleanDF(object):
	def __init__(self):
		self.df = pd.DataFrame()
	
	def left_merge(self, other, on='SEQN'):
		self.df = self.df.merge(other.df, how='left', on=on)

class DemographicDF(CleanDF):
	def __init__(self):
		self.df = pd.read_csv('../data/demographic.csv')[['SEQN','RIDAGEYR',
															'DMQMILIZ','DMDMARTL']]
		self.column_dict = {
			'DMQMILIZ': {1.0: 'Yes',2.0: 'No',7.0: np.nan,9.0: np.nan,'.': np.nan},
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
		self.df['AVG_SYS_BP'] = self.df[['BPXSY1','BPXSY2','BPXSY3','BPXSY4']].mean(axis=1)
		self.df['AVG_DIAS_BP'] = self.df[['BPXDI1','BPXDI2','BPXDI3','BPXDI4']].mean(axis=1)
		self.df['High_SYS_BP'] = self.df['AVG_SYS_BP'].apply(lambda x: int(x >= 130))
		self.df['High_DIAS_BP'] = self.df['AVG_DIAS_BP'].apply(lambda x: int(x >= 80))
	
	def drop_other_columns(self):
		self.df = self.df.drop(['BPXSY1','BPXSY2','BPXSY3','BPXSY4','BPXDI1','BPXDI2','BPXDI3','BPXDI4'],axis=1)

class LabsDF(CleanDF):
	def __init__(self):
		super(LabsDF,self).__init__()
		self.df = pd.read_csv('../data/labs.csv')[['SEQN','LBXHCT']]
	
if __name__ == '__main__':
	demo_df = DemographicDF()
	exam_df = ExamDF()