# Large-Scale Online Gaming Data Processing and Data Visualization Dashboard using Apache Spark

## 1. Project Overview
This project analyzes online gaming behavior using Apache Spark and presents meaningful insights through an interactive Streamlit dashboard.

The dataset contains 40,034 player records and 13 attributes related to gaming behavior.

## 2. Technologies Used
- Python
- Apache Spark
- PySpark
- RDD
- Spark DataFrame
- Spark SQL
- Streamlit
- Plotly
- Pandas

## 3. Main Features
- Large dataset processing using Apache Spark
- Data cleaning and validation
- RDD-based data analysis
- DataFrame operations
- Spark SQL queries
- Player engagement analysis
- Game genre analysis
- Geographical distribution analysis
- Interactive data visualization dashboard

## 4. Project Architecture
Online Gaming Dataset → PySpark → Apache Spark → RDD / DataFrame / Spark SQL → Data Cleaning and Analysis → Processed CSV Files → Streamlit Dashboard

## 5. Dataset Details
- Total records: 40,034
- Total attributes: 13
- Game genres: 5
- Locations: 4
- Engagement levels: High, Medium and Low

## 6. How to Run

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run data cleaning:

```powershell
python data_cleaning.py
```

Run Spark processing:

```powershell
python process_data.py
```

Run Spark SQL analysis:

```powershell
python spark_sql_analysis.py
```

Launch the dashboard:

```powershell
streamlit run app.py
```

## 7. Expected Output
An interactive dashboard displaying player statistics, gaming preferences, engagement patterns, geographical distribution and processed Spark analytics.

## 8. Conclusion
The project demonstrates how Apache Spark can be used to process and analyze gaming behavior data and how interactive visualization can make the resulting insights easier to understand.