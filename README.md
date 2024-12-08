# Kendrick Lamar Tracks Data Analysis
## 🚀 Overview
This project analyzes data from Kendrick Lamar's discography using visualizations to explore trends in popularity, danceability, and energy. The analysis utilizes libraries such as pandas, matplotlib, seaborn, plotly, and altair to generate static and interactive visualizations.

## 🛠 Libraries Used
The analysis relies on the following Python libraries:
- **pandas:** Data manipulation and analysis.
- **matplotlib & seaborn:** Static visualization tools.
- **plotly:** Interactive visualizations for better insights into trends.
- **altair:** Additional interactive visualizations for advanced insights.

## 📂 Dataset
### Sample Dataset Structure:
This analysis uses a dataset all_kendrick_tracks.csv. The dataset contains features about Kendrick Lamar's tracks, such as:

- release_date
- popularity
- danceability
- energy
- valence
- loudness
- speechiness
- acousticness
- instrumentalness
- tempo
- release_year
- duration_min

## 📊 Visualizations
The script generates the following visualizations:

1. Popularity Distribution: A histogram showing the distribution of track popularity.
2. Danceability vs Energy: A scatter plot analyzing the relationship between danceability, energy, and release year.
3. Average Popularity Over the Years: A line chart to track the trend in average popularity of Kendrick Lamar's tracks over the years.
4. Correlation Heatmap: Visualizes correlations between features like danceability, energy, loudness, tempo, and popularity.
5. Interactive Visualizations: Leveraging plotly and altair, interactive scatter plots are used to visualize:
   - Popularity over time.
   - Danceability vs Energy by release year.

## 💾 Processed Data
After running the analysis, the processed dataset is saved as:
> processed_kendrick_stats.csv

You can find this file in the same directory as analysis.py. This can be used for further analysis or modeling as needed.

## 🏆 Goals
The goal of this analysis is to:

- Visualize trends in danceability, energy, and popularity of Kendrick Lamar's discography tracks over time.
- Analyze correlations between these musical features and other relevant metrics.
- Explore patterns in release years, popularity trends, and features like tempo and loudness.
