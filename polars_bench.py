import polars as pl
import time
import argparse
import csv
import os   

parser = argparse.ArgumentParser(description="Example script")
parser.add_argument("--filename", type=str, required=True)
args = parser.parse_args()

start_time = time.time()
df = pl.read_csv(args.filename)
read_time = time.time() - start_time
print(f"Time to read CSV (Polars): {read_time:.4f} seconds")

start_time = time.time()
df = df.fill_null("Unknown")  
fillna_time = time.time() - start_time
print(f"Time to fill missing values (Polars): {fillna_time:.4f} seconds")

start_time = time.time()
count_reviews = df["review_text"].count()
count_time = time.time() - start_time
print(f"Time to count reviews (Polars): {count_time:.4f} seconds")

start_time = time.time()
grouped_counts = df.group_by("appid").count()
groupby_time = time.time() - start_time
print(f"Time to group by and count (Polars): {groupby_time:.4f} seconds")

file_size = os.path.getsize(args.filename) 
benchmark_results = {
    "tools": "polars",
    "file_size": file_size,
    "Read CSV": read_time,
    "Fill NA": fillna_time,
    "Count": count_time,
    "Groupby Count": groupby_time
}

csv_filename = "results.csv"

with open(csv_filename, mode="a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=benchmark_results.keys())
    writer.writerow(benchmark_results)

print(f"Benchmark results saved to {csv_filename}")