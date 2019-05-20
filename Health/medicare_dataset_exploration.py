import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns',500)

readmit = pd.read_csv('https://data.medicare.gov/resource/kac9-a9fp.csv', \
            na_values=['Not Available','Too Few to Report'])

print('Unique Start Dates: ')
print(readmit.start_date.unique())
print('Unique End Dates:')
print(readmit.end_date.unique())


readmit['my_readm_ratio'] = readmit['predicted']/readmit['expected']
readmit['pct_readmission'] = readmit['number_of_readmissions']/readmit['number_of_discharges']

readmit.hist()
plt.show()
