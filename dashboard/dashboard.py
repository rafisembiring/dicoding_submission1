import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("data\day.csv")
hour_df = pd.read_csv("data\hour.csv")

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", options=day_df["season"].unique(), default=day_df["season"].unique())
selected_weather = st.sidebar.multiselect("Pilih Cuaca", options=day_df["weathersit"].unique(), default=day_df["weathersit"].unique())

# Filter Data
df_filtered = day_df[(day_df["season"].isin(selected_season)) & (day_df["weathersit"].isin(selected_weather))]

# Title
st.title("Bike Sharing Dashboard")

# Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=df_filtered["season"], y=df_filtered["cnt"], hue=df_filtered["weathersit"], palette="Blues", ax=ax)
plt.xlabel("Season")
plt.ylabel("Total Rentals")
plt.title("Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
plt.legend(title="Weather Condition")
st.pyplot(fig)

# Jam dan Hari Paling Ramai
st.subheader("Jam dan Hari Paling Ramai untuk Penyewaan Sepeda")

# Penyewaan per jam
hourly_rentals = df_filtered.groupby("hr")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker='o', color='royalblue', ax=ax)
plt.xlabel("Hour of the Day")
plt.ylabel("Average Rentals")
plt.title("Rata-rata Penyewaan Sepeda per Jam")
st.pyplot(fig)

# Penyewaan per hari
daily_rentals = df_filtered.groupby("weekday")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=daily_rentals.index, y=daily_rentals.values, palette="Oranges", ax=ax)
plt.xlabel("Day of the Week")
plt.ylabel("Average Rentals")
plt.title("Rata-rata Penyewaan Sepeda per Hari")
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("1. Penyewaan sepeda lebih tinggi pada musim tertentu dan dipengaruhi oleh cuaca.")
st.write("2. Jam sibuk (pagi dan sore) serta akhir pekan memiliki penyewaan tertinggi.")
