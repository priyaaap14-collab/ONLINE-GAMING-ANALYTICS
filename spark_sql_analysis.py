
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Gaming Spark SQL Analysis") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Load gaming dataset
df = spark.read.csv(
    "output/cleaned_gaming_data.csv",
    header=True,
    inferSchema=True
)

# Create SQL temporary view
df.createOrReplaceTempView("gaming_data")

print("\n1. Total Number of Players")

spark.sql("""
SELECT COUNT(*) AS TotalPlayers
FROM gaming_data
""").show()

print("\n2. Number of Players by Game Genre")

spark.sql("""
SELECT GameGenre, COUNT(*) AS NumberOfPlayers
FROM gaming_data
GROUP BY GameGenre
ORDER BY NumberOfPlayers DESC
""").show()

print("\n3. Average Playtime by Game Genre")

spark.sql("""
SELECT GameGenre,
       ROUND(AVG(PlayTimeHours), 2) AS AveragePlaytime
FROM gaming_data
GROUP BY GameGenre
ORDER BY AveragePlaytime DESC
""").show()

print("\n4. Players by Engagement Level")

spark.sql("""
SELECT EngagementLevel, COUNT(*) AS NumberOfPlayers
FROM gaming_data
GROUP BY EngagementLevel
ORDER BY NumberOfPlayers DESC
""").show()

print("\n5. Average Sessions by Engagement Level")

spark.sql("""
SELECT EngagementLevel,
       ROUND(AVG(SessionsPerWeek), 2) AS AverageSessions
FROM gaming_data
GROUP BY EngagementLevel
""").show()

print("\nSpark SQL Analysis Completed Successfully!")

spark.stop()
