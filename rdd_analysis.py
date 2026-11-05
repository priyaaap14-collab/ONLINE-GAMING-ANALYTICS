import os
import sys

# Tell Spark to use the current virtual environment's Python
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Online Gaming RDD Analysis") \
    .master("local[*]") \
    .getOrCreate()

# Load dataset
df = spark.read.csv(
    "data/online_gaming_behavior_insights.csv",
    header=True,
    inferSchema=True
)

# Convert DataFrame to RDD
gaming_rdd = df.rdd

print("\n========== RDD INFORMATION ==========")

print("Number of records:", gaming_rdd.count())

# -----------------------------------------
# 1. Map operation
# Extract GameGenre
# -----------------------------------------

genre_rdd = gaming_rdd.map(lambda row: row["GameGenre"])

print("\n========== GAME GENRES USING RDD ==========")
print(genre_rdd.distinct().collect())

# -----------------------------------------
# 2. Map + ReduceByKey
# Count players by genre
# -----------------------------------------

genre_count_rdd = gaming_rdd \
    .map(lambda row: (row["GameGenre"], 1)) \
    .reduceByKey(lambda a, b: a + b)

print("\n========== PLAYER COUNT BY GENRE ==========")

for genre, count in genre_count_rdd.collect():
    print(genre, ":", count)

# -----------------------------------------
# 3. Filter operation
# Find highly engaged players
# -----------------------------------------

high_engagement_rdd = gaming_rdd.filter(
    lambda row: row["EngagementLevel"] == "High"
)

print("\n========== HIGH ENGAGEMENT PLAYERS ==========")
print("Number of high-engagement players:",
      high_engagement_rdd.count())

# -----------------------------------------
# 4. Filter + Map
# Average playtime of high-engagement players
# -----------------------------------------

high_playtime_rdd = high_engagement_rdd.map(
    lambda row: row["PlayTimeHours"]
)

total_playtime = high_playtime_rdd.sum()
player_count = high_playtime_rdd.count()

average_playtime = total_playtime / player_count

print("Average playtime of high-engagement players:",
      average_playtime)

spark.stop()