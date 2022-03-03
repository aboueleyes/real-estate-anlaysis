# merge csv
import pandas as pd
import os

# merge csv in data directory
section = 'apartments-duplex-for-sale'
csv_files = [f for f in os.listdir(f'data-{section}/') if f.endswith('.csv')]

df = pd.DataFrame()

for file in csv_files:
    try:
         df = df.append(pd.read_csv(f'data-{section}/' + file))
    except:
        print(file)

df.drop_duplicates('id', inplace=True)
df.to_csv(f'{section}.csv', index=False)
