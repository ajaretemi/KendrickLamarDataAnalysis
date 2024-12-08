# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# Step 1: Load the dataset
file_path = "all_kendrick_tracks.csv"  # Update if file is in a different location
data = pd.read_csv(file_path)

# Step 2: Inspect the dataset
print("Dataset Overview:")
print(data.head())  # Display first few rows
print("\nColumn Names:", data.columns)
print("\nDataset Info:")
print(data.info())

# Step 3: Data Cleaning and Transformation
# Convert release_date to datetime format
data['release_date'] = pd.to_datetime(data['release_date'])

# Add a new column for track duration in minutes (if not already provided)
if 'duration_min' not in data.columns:
    data['duration_min'] = data['duration_ms'] / 60000  # Convert ms to minutes

# Step 4: Visualizations

# 4.1 Popularity Distribution of Tracks
plt.figure(figsize=(8, 5))
sns.histplot(data['popularity'], kde=True, color='blue', bins=20)
plt.title("Popularity Distribution of Kendrick Lamar Tracks")
plt.xlabel("Popularity")
plt.ylabel("Count")
plt.show()

# 4.2 Danceability vs. Energy Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='danceability', y='energy', data=data, hue='release_year', palette='cool', size='popularity')
plt.title("Danceability vs Energy of Tracks")
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.legend(title='Release Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 4.3 Average Popularity Over the Years
popularity_by_year = data.groupby('release_year')['popularity'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(x='release_year', y='popularity', data=popularity_by_year, marker='o', color='green')
plt.title("Average Track Popularity Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Average Popularity")
plt.xticks(rotation=45)
plt.show()

# 4.4 Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = data[['danceability', 'energy', 'valence', 'tempo', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'popularity']].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Track Features")
plt.show()

# Create a Plotly scatter plot
fig = px.scatter(data, x='release_date', y='popularity', 
                 color='album_name', 
                 size='popularity', 
                 hover_name='track_name',
                 title="Track Popularity Over Time",
                 labels={'release_date': 'Release Date', 'popularity': 'Popularity'},
                 template="plotly_dark")

# Show the plot
fig.show()

fig = px.scatter(data, x='danceability', y='energy', 
                 color='popularity', 
                 hover_name='track_name', 
                 title="Danceability vs Energy of Kendrick Lamar's Tracks",
                 labels={'danceability': 'Danceability', 'energy': 'Energy'},
                 template="plotly")

# Show the plot
fig.show()

# Altair visualization for popularity by release year
chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('release_year:O', title='Release Year'),
    y=alt.Y('mean(popularity):Q', title='Average Popularity'),
    tooltip=['release_year', 'mean(popularity)']
).properties(
    title='Average Track Popularity by Year',
    width=700,
    height=400
).interactive()

# Show the chart
chart.show()

fig = px.scatter(data, x='danceability', y='energy',
                 facet_col='release_year', 
                 title="Danceability vs Energy Across Years")
fig.show()

# Step 5: Save Processed Data
processed_file_path = "processed_kendrick_stats.csv"
data.to_csv(processed_file_path, index=False)
print(f"Processed dataset saved to {processed_file_path}")
