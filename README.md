*# 🎮 Large-Scale Online Gaming Data Processing and Data Visualization Dashboard using Apache Spark

An end-to-end Big Data analytics project that processes and analyses **40,034 online gaming player records** using Apache Spark (PySpark), RDDs, DataFrames and Spark SQL. The analytical results are presented through an interactive dashboard developed using Streamlit and Plotly.

---

## 📌 Project Overview

Online gaming platforms generate large amounts of player-related data, including gaming preferences, playtime, session frequency, player levels and engagement patterns.

This project uses Apache Spark to process and analyse an online gaming behaviour dataset containing 40,034 records and 13 attributes.

The project demonstrates different Spark processing techniques, including RDD operations, DataFrame transformations and Spark SQL queries. The processed results are exported into CSV files and visualized through an interactive Streamlit dashboard.

The dashboard provides KPI cards, interactive filters, charts and analytical tables to help understand player behaviour and engagement patterns.

## 🎯 Project Objectives

- Process a dataset containing more than 40,000 player records using Apache Spark.
- Demonstrate Big Data processing concepts using Spark RDDs.
- Perform structured data analysis using Spark DataFrames.
- Execute analytical queries using Spark SQL.
- Validate the dataset by checking duplicate and invalid records.
- Analyse gaming genres, engagement levels, locations and difficulty preferences.
- Generate processed analytical CSV files.
- Develop an interactive visualization dashboard using Streamlit and Plotly.

## 📊 Dataset Details

**Dataset Name:** Online Gaming Behavior Insight

**Dataset Source:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/wasiqaliyasir/online-gaming-behavior-insight

| Dataset Information | Details |
|---|---|
| Total Records | 40,034 |
| Total Attributes | 13 |
| File Format | CSV |
| Data Type | Structured Data |
| Processing Type | Batch Processing |

### Dataset Attributes

The dataset contains the following 13 attributes:

1. PlayerID
2. Age
3. Gender
4. Location
5. GameGenre
6. PlayTimeHours
7. InGamePurchases
8. GameDifficulty
9. SessionsPerWeek
10. AvgSessionDurationMinutes
11. PlayerLevel
12. AchievementsUnlocked
13. EngagementLevel

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Programming Language | Python | Project implementation |
| Big Data Processing | Apache Spark (PySpark) | Data processing and aggregation |
| Processing APIs | RDD, DataFrame, Spark SQL | Different Spark analysis techniques |
| Storage | Local File System (CSV) | Store original, cleaned and processed data |
| Data Handling | Pandas | Data handling and CSV export |
| Visualization | Streamlit | Interactive dashboard |
| Charts | Plotly | Interactive data visualizations |
| Development Environment | Visual Studio Code | Project development |
| Java Environment | JDK 17 | Java environment required by Spark |

## 🏗️ System Architecture

```text
       Online Gaming Dataset
          (40,034 Records)
                  |
                  v
       Batch CSV Data Loading
              (PySpark)
                  |
                  v
           Apache Spark
              local[*]
                  |
          +-------+-------+
          |       |       |
          v       v       v
         RDD   DataFrame  Spark SQL
          |       |       |
          +-------+-------+
                  |
                  v
        Data Cleaning & Analysis
                  |
                  v
         Processed CSV Files
           (Local Storage)
                  |
                  v
         Streamlit Dashboard
                  |
                  v
            Plotly Charts
        KPIs | Filters | Tables
```

## 📁 Project Structure

The following structure is arranged according to the project's execution flow.

```text
OnlineGamingAnalytics/
│
├── data/
│   └── online_gaming_behavior_insights.csv
│
├── output/
│   ├── cleaned_gaming_data.csv
│   ├── genre_analysis.csv
│   ├── engagement_analysis.csv
│   ├── location_analysis.csv
│   └── difficulty_analysis.csv
│
├── test_spark.py
├── data_cleaning.py
├── data_analysis.py
├── rdd_analysis.py
├── process_data.py
├── spark_sql_analysis.py
├── app.py
│
├── requirements.txt
└── README.md
```

**Note:** The `venv/` and `__pycache__/` folders are excluded from the repository. The `data/` folder should contain the original Kaggle dataset. The `output/` folder stores the cleaned dataset and generated analytical CSV files.

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.11 or a compatible Python version
- JDK 17
- Visual Studio Code
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd OnlineGamingAnalytics
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Add the Dataset

Download the dataset from Kaggle:

https://www.kaggle.com/datasets/wasiqaliyasir/online-gaming-behavior-insight

Place the downloaded CSV file inside the `data/` directory.

Ensure the filename is:

```text
online_gaming_behavior_insights.csv
```

## 📦 Dependencies

The project uses the following Python libraries:

| Library | Purpose |
|---|---|
| PySpark | Big Data processing |
| Pandas | Data handling and CSV export |
| Streamlit | Dashboard development |
| Plotly | Interactive charts |
| psutil | Additional memory-management support for PySpark |

Install the dependencies using:

```bash
pip install pyspark pandas streamlit plotly psutil
```

Alternatively, install using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## ▶️ Execution Order

After activating the virtual environment and installing dependencies, execute the following scripts one after another.

### 1. Spark Initialization and Dataset Loading

```bash
python test_spark.py
```

**Purpose:**
- Initializes the SparkSession.
- Loads the original gaming dataset.
- Displays the dataset schema.
- Verifies the total number of records.

### 2. Data Cleaning

```bash
python data_cleaning.py
```

**Purpose:**
- Checks duplicate records.
- Validates selected numerical attributes.
- Generates the cleaned dataset.
- Saves the cleaned data as `cleaned_gaming_data.csv`.

### 3. DataFrame Analysis

```bash
python data_analysis.py
```

**Purpose:**
- Analyses player distribution by game genre.
- Calculates average playtime across genres.
- Analyses player engagement levels.
- Examines player distribution across locations.

### 4. RDD Analysis

```bash
python rdd_analysis.py
```

**Purpose:**

Demonstrates Spark RDD transformations and actions:

- `map()`
- `filter()`
- `distinct()`
- `reduceByKey()`
- `count()`
- `sum()`

### 5. Data Processing and Export

```bash
python process_data.py
```

**Purpose:**

Generates analytical CSV files inside the `output/` directory:

- `genre_analysis.csv`
- `engagement_analysis.csv`
- `location_analysis.csv`
- `difficulty_analysis.csv`

### 6. Spark SQL Analysis

```bash
python spark_sql_analysis.py
```

**Purpose:**
- Creates a temporary SQL view.
- Executes SQL queries on the cleaned gaming dataset.
- Analyses total players, game genres, average playtime and engagement levels.

### 7. Launch the Interactive Dashboard

```bash
streamlit run app.py
```

**Purpose:**
- Displays the interactive gaming analytics dashboard.
- Shows KPI cards and charts.
- Provides filters for game genre, engagement level, location and game difficulty.
- Displays processed analytical tables.

The dashboard will usually open at:

`http://localhost:8501`

## 📈 Dashboard Features

The interactive dashboard includes:

### KPI Cards

- Total Players
- Average Playtime
- Number of Game Genres
- Number of Locations

### Interactive Visualizations

- Players by Game Genre
- Engagement Distribution
- Players by Location
- Game Difficulty Distribution
- Average Sessions per Week by Engagement
- Average Achievements by Engagement

### Interactive Filters

Users can filter the dashboard based on:

- Game Genre
- Engagement Level
- Location
- Game Difficulty

### Analytical Tables

The dashboard also displays processed Spark analysis results through separate tabs for:

- Genre Analysis
- Engagement Analysis
- Location Analysis
- Difficulty Analysis

## 📊 Key Results and Insights

The analysis of 40,034 player records produced the following results.

### 1. Players by Game Genre

| Game Genre | Number of Players |
|---|---:|
| Sports | 8,048 |
| Action | 8,039 |
| Strategy | 8,012 |
| Simulation | 7,983 |
| RPG | 7,952 |

### 2. Player Engagement Distribution

| Engagement Level | Number of Players |
|---|---:|
| Medium | 19,374 |
| High | 10,336 |
| Low | 10,324 |

### 3. Player Distribution by Location

| Location | Number of Players |
|---|---:|
| USA | 16,000 |
| Europe | 12,004 |
| Asia | 8,095 |
| Other | 3,935 |

### 4. Important Observations

- Sports has the highest player count among the five game genres.
- Medium engagement represents the largest player group.
- USA has the highest number of players in the dataset.
- High-engagement players average approximately 14.25 gaming sessions per week, compared with approximately 4.53 for low-engagement players.
- Data validation identified zero duplicate records and zero invalid records under the implemented checks.
- The average playtime across different genres is relatively similar.

## 💾 Storage and Processing

- The original dataset is stored as a CSV file in the local `data/` directory.
- The cleaned dataset and analytical outputs are stored as CSV files in the `output/` directory.
- Apache Spark performs data processing in local mode using `local[*]`.
- Pandas is used to export the processed analytical results.
- The Streamlit dashboard reads the generated analytical CSV files.

## ⚠️ Limitations

- Apache Spark runs in local mode and is not deployed on a multi-node cluster.
- The project uses static batch CSV input instead of real-time data ingestion.
- HDFS, Kafka, cloud storage and NoSQL databases are not implemented.
- The dataset does not contain timestamps for time-based trend analysis.
- Machine learning and predictive modelling are outside the current project scope.
- The dashboard uses precomputed CSV outputs rather than directly executing Spark jobs for every interaction.

## 🚀 Future Enhancements

- Integrate larger gaming datasets.
- Deploy Apache Spark on a multi-node cluster.
- Introduce real-time data ingestion using Apache Kafka.
- Integrate distributed storage such as HDFS.
- Add machine learning models for player engagement prediction.
- Implement player segmentation and recommendation systems.
- Integrate database storage and cloud deployment.

## 📚 References

- Apache Spark Documentation: https://spark.apache.org/docs/latest/
- PySpark Documentation: https://spark.apache.org/docs/latest/api/python/
- Streamlit Documentation: https://docs.streamlit.io/
- Plotly Documentation: https://plotly.com/python/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Kaggle Dataset: https://www.kaggle.com/datasets/wasiqaliyasir/online-gaming-behavior-insight

the repository a star!

