import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([ range(1, 11), range(11, 21), range(21, 31)]).T,
                  columns=['A', 'B', 'C'])
print(df)

data = np.array([ range(1, 11), range(11, 21), range(21, 31)])

df2 = pd.DataFrame(data, columns=[f'col{i}' for i in range(1, 11)])

print(df2)

"""
data = np.array([range(1, 11), range(11, 21), range(21, 31)])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

"""
