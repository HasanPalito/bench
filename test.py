import modin.pandas as pd

df = pd.DataFrame({"A": range(10000), "B": range(10000)})
partitions = df._query_compiler._modin_frame._partitions
print(len(partitions))
partition = partitions[0][0]
pandas_df = partition.to_pandas()

print(pandas_df)
