from pyspark.sql import SparkSession
import time
import argparse
import csv
import os

parser = argparse.ArgumentParser(description="Example script")
parser.add_argument("--filename", type=str, required=True)
args = parser.parse_args()

spark = SparkSession.builder.appName("BenchmarkReviews").getOrCreate()

start_time = time.time()
df = spark.read.csv(args.filename, header=True, inferSchema=True)
read_time = time.time() - start_time
print(f"Time to read CSV (PySpark): {read_time:.4f} seconds")

start_time = time.time()
df = df.fillna({"review_text": "Unknown"})  # PySpark equivalent of fillna
fillna_time = time.time() - start_time
print(f"Time to fill missing values (PySpark): {fillna_time:.4f} seconds")

start_time = time.time()
count_reviews = df.count()
count_time = time.time() - start_time
print(f"Time to count reviews (PySpark): {count_time:.4f} seconds")

start_time = time.time()
grouped_counts = df.groupby("review_score").count()
groupby_time = time.time() - start_time
print(f"Time to group by and count (Polars): {groupby_time:.4f} seconds")

file_size = os.path.getsize(args.filename) 
benchmark_results = {
    "tools": "spark",
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