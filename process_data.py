import os
import sys

# Fix Python worker issue on Windows
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Start Spark
spark = SparkSession.builder \
    .appName("Online Gaming Analytics") \
    .master("local[*]") \
    .getOrCreate()

print("\n========================================")
print("   ONLINE GAMING ANALYTICS")
print("   Apache Spark Processing Pipeline")
print("========================================\n")

# Load dataset
df = spark.read.csv(
    "data/online_gaming_behavior_insights.csv",
    header=True,
    inferSchema=True
)

print("Dataset loaded successfully!")
print("Total records:", df.count())


# ------------------------------------------------
# 1. GENRE ANALYSIS
# ------------------------------------------------

print("\n========== GENRE ANALYSIS ==========")

genre_analysis = df.groupBy("GameGenre").agg(
    count("*").alias("NumberOfPlayers"),
    avg("PlayTimeHours").alias("AveragePlayTime")
).orderBy("GameGenre")

genre_analysis.show()


# ------------------------------------------------
# 2. ENGAGEMENT ANALYSIS
# ------------------------------------------------

print("\n========== ENGAGEMENT ANALYSIS ==========")

engagement_analysis = df.groupBy("EngagementLevel").agg(
    count("*").alias("NumberOfPlayers"),
    avg("PlayTimeHours").alias("AveragePlayTime"),
    avg("SessionsPerWeek").alias("AverageSessions"),
    avg("AchievementsUnlocked").alias("AverageAchievements")
).orderBy("EngagementLevel")

engagement_analysis.show()


# ------------------------------------------------
# 3. LOCATION ANALYSIS
# ------------------------------------------------

print("\n========== LOCATION ANALYSIS ==========")

location_analysis = df.groupBy("Location").agg(
    count("*").alias("NumberOfPlayers"),
    avg("PlayTimeHours").alias("AveragePlayTime")
).orderBy("Location")

location_analysis.show()


# ------------------------------------------------
# 4. GAME DIFFICULTY ANALYSIS
# ------------------------------------------------

print("\n========== DIFFICULTY ANALYSIS ==========")

difficulty_analysis = df.groupBy("GameDifficulty").agg(
    count("*").alias("NumberOfPlayers"),
    avg("PlayTimeHours").alias("AveragePlayTime"),
    avg("SessionsPerWeek").alias("AverageSessions")
).orderBy("GameDifficulty")

difficulty_analysis.show()


# ------------------------------------------------
# SAVE PROCESSED RESULTS
# ------------------------------------------------

os.makedirs("output", exist_ok=True)

# Spark performs the processing above.
# Pandas is used only after aggregation to save
# the small summary tables as CSV files.

genre_analysis.toPandas().to_csv(
    "output/genre_analysis.csv",
    index=False
)

engagement_analysis.toPandas().to_csv(
    "output/engagement_analysis.csv",
    index=False
)

location_analysis.toPandas().to_csv(
    "output/location_analysis.csv",
    index=False
)

difficulty_analysis.toPandas().to_csv(
    "output/difficulty_analysis.csv",
    index=False
)


print("\n========================================")
print("Processing completed successfully!")
print("Results saved in the output folder.")
print("========================================")

spark.stop()