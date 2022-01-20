import pandas as pd
import numpy as np


def convert(x):
    try:
        retval = float(x.replace(',', '', -1))
    except:
        retval = x
    return retval


def a(x):
    try:
        xx = float(x.replace(',', '', -1))
    except:
        xx = np.nan
    return xx


data = [{'a': '2,325,147', 'b': '2.1'}, {'a': '5', 'b': 'test'}]
df = pd.DataFrame(data)

new_df = df.apply(np.vectorize(a))


