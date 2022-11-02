# import packages
import pandas as pd
import tableone as t1
import researchpy as rp
import numpy as np
from scipy import stats
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas.plotting as plotting
from statsmodels.formula.api import ols
from tableone import TableOne, load_dataset 



##### DATASET 1 #####
# import data 
my_data = pd.read_csv('data/newborn_screening.csv')
my_data.columns
my_data

df1 = my_data.copy()
df1.dtypes
list(df1)
df1.head(5)

df1_columns = ['Race/Ethnicity', 'Disorder Type']
p = p.reindex(columns=columns)
df1_categories = ['Race/Ethincity', 'Disorder Type']
df1_groupby = ['Disorder Type']
df1_table1 = TableOne(df1, columns=df1_columns, categorical=df1_categories, groupby=df1_groupby,  pval=False)
print(df1_table1.tabulate(tablefmt = "fancy_grid"))
df1_table1.to_csv('/Users/corinne/Documents/GitHub/descriptives-scipy/data/test.csv')

#codebook 
rp.codebook(my_data)
# descrptives for continous variables 
my_data.columns 
rp.summary_cont(my_data[['Screened\nCount','Disorder\nCount', 'Rate\nper\n100,000']])
rp.summary_cat(my_data[['Race/Ethnicity', 'Disorder Type']])
my_data['Race/Ethnicity'].value_counts()
my_data['Disorder Type'].value_counts()

##### DATASET 2 #####
example_data = load_dataset('pn2012')
# # littlerecode death where 0 is alive and 1 is dead
# example_data['death'] = example_data['death'].replace(0, 'alive')
example_data.dtypes
example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']
example_data_categorical = ['ICU', 'death']
example_data_groupby = ['death']
example_data_labels={'death': 'mortality'}
exampleTab1 = TableOne(example_data, columns=example_data_columns, categorical=example_data_categorical, groupby=example_data_groupby, rename=example_data_labels, pval=False)
exampleTab1
print(exampleTab1.tabulate(tablefmt = "fancy_grid"))
exampleTab1.to_csv('/Users/corinne/Documents/GitHub/descriptives-scipy/data/test2.csv')

#scipy website code 

df = pd.read_csv('data/brain_size.csv')
df

#array 
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)
pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})   

#t-test
group1_viq = data[data['Group'] == 'Active']['Age']
group2_viq = data[data['Group'] == 'Control']['Age']
stats.ttest_ind(group1_viq, group2_viq)

#linear regression 
x = np.linspace(-5, 5, 20)
np.random.seed(1)
y = -5 + 3 * x + 4 * np.random.normal(size=x.shape)
data = pd.DataFrame({'x': x, 'y': y})

#t-test cont 
data_fisq = pd.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pd.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pd.concat((data_fisq, data_piq))
print(data_long)  
model = ols("iq ~ type", data_long).fit()
print(model.summary())  