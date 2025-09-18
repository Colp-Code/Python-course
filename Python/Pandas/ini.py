import pandas as pd
import numpy as np
import seaborn as sns
# Load the Titanic dataset from seaborn and 
tic = sns.load_dataset('titanic')
# Display the first three ages I used the head() function to get the first three entries
age = tic["age"].head(3)
print(age)
# Display the first ten ages using iloc to get the first ten entries
# iloc is used for interger-location based indexing for example iloc[0:10] gets the first ten rows
# iloc is useful when you want to select rows based on their integer position in the DataFrame
age_2 = tic.age.iloc[0:10]
print(age_2)