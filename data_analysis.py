from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, sum, desc

spark = SparkSession.builder \
    .appName("Online Gaming Analytics") \
    .master("local[*]") \
    .getOrCreate()

# Load dataset
df = spark.read.csv(
    "data/online_gaming_behavior_insights.csv",
    header=True,
    inferSchema=True
)

print("\n========== DATASET INFORMATION ==========")

print("Total Records:", df.count())
print("Total Columns:", len(df.columns))

print("\n========== COLUMNS ==========")
df.printSchema()

print("\n========== FIRST 10 RECORDS ==========")
df.show(10, truncate=False)

# -----------------------------------------
# 1. Players by Game Genre
# -----------------------------------------

print("\n========== PLAYERS BY GAME GENRE ==========")

genre_count = df.groupBy("GameGenre") \
    .agg(count("PlayerID").alias("NumberOfPlayers")) \
    .orderBy(desc("NumberOfPlayers"))

genre_count.show()

# -----------------------------------------
# 2. Average Playtime by Genre
# -----------------------------------------

print("\n========== AVERAGE PLAYTIME BY GENRE ==========")

playtime_genre = df.groupBy("GameGenre") \
    .agg(avg("PlayTimeHours").alias("AveragePlayTime")) \
    .orderBy(desc("AveragePlayTime"))

playtime_genre.show()

# -----------------------------------------
# 3. Engagement Level Distribution
# -----------------------------------------

print("\n========== ENGAGEMENT LEVEL ==========")

engagement = df.groupBy("EngagementLevel") \
    .agg(count("PlayerID").alias("NumberOfPlayers")) \
    .orderBy(desc("NumberOfPlayers"))

engagement.show()

# -----------------------------------------
# 4. Average Sessions by Engagement
# -----------------------------------------

print("\n========== SESSIONS BY ENGAGEMENT ==========")

sessions = df.groupBy("EngagementLevel") \
    .agg(
        avg("SessionsPerWeek").alias("AverageSessions"),
        avg("PlayTimeHours").alias("AveragePlayTime")
    ) \
    .orderBy(desc("AverageSessions"))

sessions.show()

# -----------------------------------------
# 5. Location-wise Players
# -----------------------------------------

print("\n========== PLAYERS BY LOCATION ==========")

location = df.groupBy("Location") \
    .agg(count("PlayerID").alias("NumberOfPlayers")) \
    .orderBy(desc("NumberOfPlayers"))

location.show()

spark.stop()