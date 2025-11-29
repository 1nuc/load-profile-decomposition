import pandas as pd
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pathlib import Path
import polars.selectors as cs
from scipy import stats


class loadProfile:
    def __init__(self,data):
        self.data=data
        self.devices=[n for n in data.columns if n.startswith('out.electricity')]
        self.dev_count=len(self.devices)
        plt.style.use('ggplot')
        
    def boxplot_exp(self):
        fig, ax=plt.subplots(self.dev_count, 1, figsize=(10, 7 * self.dev_count))
        for i,x in enumerate(self.devices):
            sns.boxplot(data=self.data, x=x, ax=ax[i])
    
    def hist_exp(self):
        fig, ax=plt.subplots(self.dev_count, 1, figsize=(10, 7 * self.dev_count))
        for i,x in enumerate(self.devices):
            sns.histplot(data=self.data, x=x, ax=ax[i])
                
    def boxen_exp(self):
        fig, ax=plt.subplots(self.dev_count, 1, figsize=(10, 7 * self.dev_count))
        for i,x in enumerate(self.devices):
            sns.boxenplot(data=self.data, x=x, ax=ax[i])
    
    def edit_column_names(self,df):
        df=df.rename(lambda col: col.replace('.energy_consumption..kwh', ''))
        return df
    def barplot_seaborn(self,x,y):
        plot=sns.barplot(
            data=self.data, 
            x=x, 
            y=y, 
            hue=y, estimator='sum')
        
        plot.set(xlabel)
    def test_corr(df,var):
        cols=[col for col in df.columns if col.startswith('out.electricity') and col != var]
        arr=[]
        for col in cols:
            p_corr, p_val=stats.pearsonr(df[col], df[var])
            df_test=pd.DataFrame({
            "p_value":[p_val],
            "pearson correlation:" : [p_corr],
            "col": [col]})
            arr.append(df_test)
        return pd.concat(arr)