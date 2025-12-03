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
            plot=sns.boxplot(data=self.data, x=x, ax=ax[i])
            xlabel=x.removeprefix("out.electricity.")
            plot.set(xlabel=xlabel, ylabel="count")
    
    def hist_exp(self):
        fig, ax=plt.subplots(self.dev_count, 1, figsize=(10, 7 * self.dev_count))
        for i,x in enumerate(self.devices):
            plot=sns.histplot(data=self.data, x=x, ax=ax[i])
            xlabel=x.removeprefix("out.electricity.")
            plot.set(xlabel=xlabel, ylabel="count")
                
    def boxen_exp(self):
        fig, ax=plt.subplots(self.dev_count, 1, figsize=(10, 7 * self.dev_count))
        for i,x in enumerate(self.devices):
            plot=sns.boxenplot(data=self.data, x=x, ax=ax[i])
            xlabel=x.removeprefix("out.electricity.")
            plot.set(xlabel=xlabel, ylabel="count")
    
    def edit_column_names(self,df):
        df=df.rename(lambda col: col.replace('in.','') if col.startswith('in.') else col.replace('.energy_consumption..kwh', ''))
        return df

    def barplot_seaborn(self,x,y):
        plot=sns.barplot(
            data=self.data, 
            x=x, 
            y=y, 
            hue=y, estimator='sum')
    
    def barplot_mat(self,x,y):
        plt.barplot(
            data=self.data, 
            x=x, 
            y=y, 
            hue=y, estimator='sum')
        
    def test_corr(df,var):
        cols=[col for col in df.columns if col.startswith('out.electricity') and col != var]
        arr=[]
        for col in cols:
            p_corr, p_val=stats.pearsonr(df[col], df[var])
            df_test=pd.DataFrame({
                "p_value":[p_val],
                "pearson correlation:": [p_corr],
                "col": [col]
            })
            arr.append(df_test)
        return pd.concat(arr)
    
    def display_totals(self,df, x, y):
        sns.jointplot(data=df, x=x, y=y, kind='reg')
        
    # visualizing long duration devices per each hour of the day by having a barplot
    def long_dev_temporal_based(self,df, temporal_type):
        cols=[col for col in df.columns if col.startswith('out.electricity')]
        for col in cols:
            plt.figure(figsize=(20,8))
            plot=sns.barplot(data=df, x=temporal_type, y=col, color='purple')
            label=col.removeprefix('out.electricity.')
            plot.set(xlabel=temporal_type, ylabel=label)
            plt.show()
            
    def test_corr(self,df,var):
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
    
    def _barplot_seaborn(self,data,x,y):
        plt.figure(figsize=(20, 8))
        plot=sns.barplot(
            data=data, 
            x=x, 
            y=y, 
            hue=y, estimator='sum')
