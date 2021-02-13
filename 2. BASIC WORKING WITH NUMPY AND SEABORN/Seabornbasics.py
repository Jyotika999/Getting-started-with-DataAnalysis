import numpy as np
import pandas as pd
import seaborn as sns

arr_ex = np.random.randn(4,4)

sns.distplot(pd.DataFrame(arr_ex.reshape(16,1)))

np.random.randint(0,100,8).reshape(4,2)