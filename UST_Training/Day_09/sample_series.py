import numpy as np
import pandas as pd

arr=np.array([1,2,3,4,5])
series_obj =pd.Series(arr,index=['a','b','c','d','e'])
print(series_obj)
