import pandas as pd
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pathlib import Path
import polars.selectors as cs

class exploration:
    def __init__(self,data):
        self.data=data
        self.devices=[n for n in data.columns if n.startswith('out.electricity')]
        self.dev_count=len(self.devices)
        
        