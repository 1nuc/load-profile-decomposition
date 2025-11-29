import pandas as pd
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pathlib import Path
import polars.selectors as cs

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
            sns.boxenplot(data=self.data, x=x, y='timestamp', ax=ax[i])