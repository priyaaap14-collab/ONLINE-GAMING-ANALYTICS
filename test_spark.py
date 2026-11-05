from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Online Gaming Analytics") \
    .master("local[*]") \
    .getOrCreate()

print("Spark started successfully!")

# Load the gaming dataset
df = spark.read.csv(
    "data/online_gaming_behavior_insights.csv",
    header=True,
    inferSchema=True
)

# Display number of records
print("Number of records:", df.count())

# Display number of columns
print("Number of columns:", len(df.columns))

# Display column names
print("\nColumns:")
print(df.columns)

# Display first 5 rows
print("\nFirst 5 rows:")
df.show(5, truncate=False)

# Display data types
print("\nData types:")
df.printSchema()

# Stop Spark
spark.stop()