import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Online Gaming Analytics",
    page_icon="🎮",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎮 Online Gaming Analytics Dashboard")
st.caption("Large-Scale Online Gaming Data Processing using Apache Spark")


# --------------------------------------------------
# LOAD PROCESSED DATA
# --------------------------------------------------

genre_df = pd.read_csv("output/genre_analysis.csv")
engagement_df = pd.read_csv("output/engagement_analysis.csv")
location_df = pd.read_csv("output/location_analysis.csv")
difficulty_df = pd.read_csv("output/difficulty_analysis.csv")


# --------------------------------------------------
# KPI VALUES
# --------------------------------------------------

total_players = genre_df["NumberOfPlayers"].sum()

avg_playtime = (
    genre_df["AveragePlayTime"] * genre_df["NumberOfPlayers"]
).sum() / total_players

total_genres = genre_df["GameGenre"].nunique()

total_locations = location_df["Location"].nunique()


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Players",
        f"{total_players:,}"
    )

with col2:
    st.metric(
        "⏱️ Avg Playtime",
        f"{avg_playtime:.2f} hrs"
    )

with col3:
    st.metric(
        "🎮 Game Genres",
        total_genres
    )

with col4:
    st.metric(
        "🌍 Locations",
        total_locations
    )


st.divider()


# --------------------------------------------------
# SIDEBAR FILTER
# --------------------------------------------------

st.sidebar.header("🎯 Filters")

selected_genre = st.sidebar.multiselect(
    "Game Genre",
    options=genre_df["GameGenre"].unique(),
    default=genre_df["GameGenre"].unique()
)

selected_engagement = st.sidebar.multiselect(
    "Engagement Level",
    options=engagement_df["EngagementLevel"].unique(),
    default=engagement_df["EngagementLevel"].unique()
)

selected_location = st.sidebar.multiselect(
    "Location",
    options=location_df["Location"].unique(),
    default=location_df["Location"].unique()
)

selected_difficulty = st.sidebar.multiselect(
    "Game Difficulty",
    options=difficulty_df["GameDifficulty"].unique(),
    default=difficulty_df["GameDifficulty"].unique()
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_genre = genre_df[
    genre_df["GameGenre"].isin(selected_genre)
]

filtered_engagement = engagement_df[
    engagement_df["EngagementLevel"].isin(selected_engagement)
]

filtered_location = location_df[
    location_df["Location"].isin(selected_location)
]

filtered_difficulty = difficulty_df[
    difficulty_df["GameDifficulty"].isin(selected_difficulty)
]


# --------------------------------------------------
# ROW 1 — GENRE + ENGAGEMENT
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("🎮 Players by Game Genre")

    fig_genre = px.bar(
        filtered_genre,
        x="GameGenre",
        y="NumberOfPlayers",
        text="NumberOfPlayers",
        title="Number of Players by Genre"
    )

    fig_genre.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig_genre,
        use_container_width=True
    )


with col2:

    st.subheader("📊 Engagement Distribution")

    fig_engagement = px.pie(
        filtered_engagement,
        names="EngagementLevel",
        values="NumberOfPlayers",
        hole=0.4,
        title="Player Engagement Levels"
    )

    st.plotly_chart(
        fig_engagement,
        use_container_width=True
    )


# --------------------------------------------------
# ROW 2 — LOCATION + DIFFICULTY
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("🌍 Players by Location")

    fig_location = px.bar(
        filtered_location,
        x="Location",
        y="NumberOfPlayers",
        text="NumberOfPlayers",
        title="Geographical Distribution"
    )

    fig_location.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig_location,
        use_container_width=True
    )


with col2:

    st.subheader("⚔️ Game Difficulty")

    fig_difficulty = px.bar(
        filtered_difficulty,
        x="GameDifficulty",
        y="NumberOfPlayers",
        text="NumberOfPlayers",
        title="Players by Game Difficulty"
    )

    fig_difficulty.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig_difficulty,
        use_container_width=True
    )


# --------------------------------------------------
# ROW 3 — ENGAGEMENT ANALYSIS
# --------------------------------------------------

st.divider()

st.subheader("🔥 Engagement Behavior Analysis")

col1, col2 = st.columns(2)


with col1:

    fig_sessions = px.bar(
        filtered_engagement,
        x="EngagementLevel",
        y="AverageSessions",
        text="AverageSessions",
        title="Average Sessions per Week by Engagement"
    )

    fig_sessions.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig_sessions,
        use_container_width=True
    )


with col2:

    fig_achievements = px.bar(
        filtered_engagement,
        x="EngagementLevel",
        y="AverageAchievements",
        text="AverageAchievements",
        title="Average Achievements by Engagement"
    )

    fig_achievements.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig_achievements,
        use_container_width=True
    )


# --------------------------------------------------
# DATA TABLES
# --------------------------------------------------

st.divider()

st.subheader("📋 Processed Spark Analytics")

tab1, tab2, tab3, tab4 = st.tabs([
    "Genre",
    "Engagement",
    "Location",
    "Difficulty"
])


with tab1:
    st.dataframe(
        filtered_genre,
        use_container_width=True
    )

with tab2:
    st.dataframe(
        filtered_engagement,
        use_container_width=True
    )

with tab3:
    st.dataframe(
        filtered_location,
        use_container_width=True
    )

with tab4:
    st.dataframe(
        filtered_difficulty,
        use_container_width=True
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------


st.divider()

st.caption(
    "Built using Python • PySpark • Apache Spark • Streamlit • Plotly"
)