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

# Distribusi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=day_df['season'], y=day_df['cnt'], palette='Set2', ax=ax)
plt.xlabel("Season")
plt.ylabel("Total Rentals")
plt.title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("1. Penyewaan sepeda lebih tinggi pada musim panas dan lebih rendah pada musim dingin.")
st.write("2. Cuaca buruk mengurangi jumlah penyewaan sepeda secara signifikan.")
st.write("3. Penyewaan sepeda paling ramai terjadi pada jam sibuk pagi (07:00 - 09:00) dan sore (17:00 - 19:00).")
st.write("4. Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan akhir pekan.")
st.write("5. Rekomendasi: Meningkatkan jumlah sepeda saat jam sibuk dan memberikan promosi di musim dingin.")
