import polars as pl

df = pl.read_csv("dataset.csv")

df = df.rename({"app_id": "appid"})

df.write_csv("dataset.csv")
