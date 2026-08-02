import sys

import pandas as pd

df = pd.DataFrame({'a':[1,2],'b':[3,4]})
print('arguments', sys.argv)

month = int(sys.argv[1])

df.to_parquet(f"Output_{month}.parquet")
print(f'hello pipeline, month={month}')

