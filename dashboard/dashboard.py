import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset with universal path
base_dir = os.path.dirname(__file__)
day_df = pd.read_csv(os.path.join(base_dir, "../data/day.csv"))
hour_df = pd.read_csv(os.path.join(base_dir, "../data/hour.csv"))

# Sidebar Filters
st.sidebar.header("Filter Data")
season_options = ["All"] + sorted(day_df["season"].unique().tolist())
weather_options = ["All"] + sorted(day_df["weathersit"].unique().tolist())
selected_season = st.sidebar.multiselect("Pilih Musim", options=season_options, default=["All"])
selected_weather = st.sidebar.multiselect("Pilih Cuaca", options=weather_options, default=["All"])

# Filter Data
filtered_df = day_df.copy()
if "All" not in selected_season:
    filtered_df = filtered_df[filtered_df["season"].isin(selected_season)]
if "All" not in selected_weather:
    filtered_df = filtered_df[filtered_df["weathersit"].isin(selected_weather)]

# Title
st.title("Bike Sharing Dashboard")

# Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=filtered_df["season"], y=filtered_df["cnt"], hue=filtered_df["weathersit"], palette="Set2", ax=ax)
plt.xlabel("Season")
plt.ylabel("Total Rentals")
plt.title("Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
plt.legend(title="Weather Condition")
st.pyplot(fig)

# Jam dan Hari Paling Ramai
st.subheader("Jam dan Hari Paling Ramai untuk Penyewaan Sepeda")

# Penyewaan per jam
hourly_rentals = hour_df.groupby("hr")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker='o', color='royalblue', ax=ax)
plt.xlabel("Hour of the Day")
plt.ylabel("Average Rentals")
plt.title("Rata-rata Penyewaan Sepeda per Jam")
st.pyplot(fig)

# Penyewaan per hari
daily_rentals = day_df.groupby("weekday")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=daily_rentals.index, y=daily_rentals.values, palette="coolwarm", ax=ax)
plt.xlabel("Day of the Week")
plt.ylabel("Average Rentals")
plt.title("Rata-rata Penyewaan Sepeda per Hari")
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("1. Penyewaan sepeda lebih tinggi pada musim tertentu dan dipengaruhi oleh cuaca.")
st.write("2. Jam sibuk (pagi dan sore) serta akhir pekan memiliki penyewaan tertinggi.")
