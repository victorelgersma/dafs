
import pandas as pd

df = pd.read_csv("test_data.csv")

# https://jpvdp.github.io/NetworkIsLife/

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html

# import test_data
print(df)

df["one"] = (df["two"] * 4)

print(df)