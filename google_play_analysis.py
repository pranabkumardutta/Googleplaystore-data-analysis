import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_csv('googleplaystore.csv')

# Clean data: Handle any missing values or incorrect data
df.dropna(subset=['Rating'], inplace=True)  # Drop rows with missing ratings
# Replace commas, plus signs and non-numeric values with 0
df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '')

# Replace non-numeric values like 'Free' with 0
df['Installs'] = df['Installs'].replace('Free', '0')

# Convert the 'Installs' column to integers
df['Installs'] = df['Installs'].astype(int)
df['Reviews'] = df['Reviews'].replace({'M': 'e6', 'K': 'e3'}, regex=True)

# Step 2: Convert 'Reviews' to numeric, coercing errors to NaN
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

# Step 3: Calculate the average of the 'Reviews' column
average_reviews = df['Reviews'].mean()

print(f"Average Reviews: {average_reviews}")

# Streamlit Title
st.title('Google Play Store Data Analysis')

# Display the first 5 rows of the dataset
st.subheader('Top 5 Rows of the Dataset')
st.write(df.head())

# Display the last 3 rows of the dataset
st.subheader('Last 3 Rows of the Dataset')
st.write(df.tail(3))

# Shape of the dataset
st.subheader('Shape of the Dataset')
st.write(f"Number of Apps: {df.shape[0]}")
st.write(f"Number of Columns: {df.shape[1]}")

# Info about the dataset
st.subheader('Dataset Information')
st.write(df.info())

# Descriptive statistics
st.subheader('Descriptive Statistics')
st.write(df.describe(include='all'))

# Find the total number of apps containing 'Astrology' in the name
astrology_apps = df[df['App'].str.contains('Astrology', case=False)]
st.subheader('Apps containing Astrology in the name')
st.write(astrology_apps)
st.write(f"Total number of Astrology apps: {len(astrology_apps)}")

# Average rating
average_rating = df['Rating'].mean()
st.subheader('Average App Rating')
st.write(f"The average rating of apps: {average_rating:.2f}")

# Find total number of unique categories
unique_categories = df['Category'].nunique()
st.subheader('Total Number of Unique Categories')
st.write(f"There are {unique_categories} unique categories in the dataset.")

# Find the category with the highest average rating
highest_avg_rating_category = df.groupby('Category')['Rating'].mean().idxmax()
st.subheader('Category with Highest Average Rating')
st.write(f"The category with the highest average rating is {highest_avg_rating_category}.")

# Total number of apps with 5-star rating
five_star_apps = df[df['Rating'] == 5]
st.subheader('Apps with 5-Star Rating')
st.write(f"Total number of apps with a 5-star rating: {len(five_star_apps)}")

# Average reviews
average_reviews = df['Reviews'].mean()
st.subheader('Average Value of Reviews')
st.write(f"The average number of reviews is {average_reviews:.2f}")

# Total number of Free and Paid Apps
free_paid_apps = df['Type'].value_counts()
st.subheader('Total Number of Free and Paid Apps')
st.write(free_paid_apps)

# App with maximum reviews
max_reviews_app = df[df['Reviews'] == df['Reviews'].max()]
st.subheader('App with Maximum Reviews')
st.write(max_reviews_app[['App', 'Reviews']])

# Top 5 apps with highest reviews
top_5_reviews = df.nlargest(5, 'Reviews')
st.subheader('Top 5 Apps with Highest Reviews')
st.write(top_5_reviews[['App', 'Reviews']])

# Average rating of free and paid apps
avg_rating_free_paid = df.groupby('Type')['Rating'].mean()
st.subheader('Average Rating of Free and Paid Apps')
st.write(avg_rating_free_paid)

# Top 5 apps with maximum installs
top_5_installs = df.nlargest(5, 'Installs')
st.subheader('Top 5 Apps with Maximum Installs')
st.write(top_5_installs[['App', 'Installs']])

# Visualizations
# Plotting the number of apps per category
st.subheader('Number of Apps in Each Category')
category_counts = df['Category'].value_counts()
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Apps per Category')
plt.xlabel('Category')
plt.ylabel('Number of Apps')
st.pyplot()

# Plotting the average rating per category
st.subheader('Average Rating per Category')
category_avg_rating = df.groupby('Category')['Rating'].mean()
category_avg_rating.sort_values(ascending=False).head(10).plot(kind='bar', color='orange', figsize=(10, 6))
plt.title('Top 10 Categories with Highest Average Rating')
plt.xlabel('Category')
plt.ylabel('Average Rating')
st.pyplot()

# Plotting the distribution of app ratings
st.subheader('Distribution of App Ratings')
plt.figure(figsize=(8, 5))
sns.histplot(df['Rating'], kde=True, bins=30)
plt.title('Distribution of App Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
st.pyplot()

# Show Streamlit app
st.write("Explore the data interactively!")
