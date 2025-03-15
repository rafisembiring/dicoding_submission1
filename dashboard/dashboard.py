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

# Rata-rata Penyewaan Sepeda Berdasarkan Musim dan Cuaca
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=day_df["season"], y=day_df["cnt"], hue=day_df["weathersit"], palette="Set2", ax=ax)
plt.xticks(ticks=[0,1,2,3], labels=["Spring", "Summer", "Fall", "Winter"])
plt.xlabel("Musim")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.title("Tren Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
plt.legend(title="Kondisi Cuaca", labels=["Cerah", "Mendung", "Hujan/Salju Ringan", "Hujan Deras"])
st.pyplot(fig)

# Tren Penyewaan Sepeda Berdasarkan Jam
st.subheader("Rata-rata Penyewaan Sepeda per Jam")
hourly_rentals = hour_df.groupby("hr")["cnt"].mean()
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker='o', color='blue', ax=ax)
plt.xlabel("Jam dalam Sehari")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.title("Rata-rata Penyewaan Sepeda per Jam")
plt.xticks(ticks=range(0, 24))
plt.grid()
st.pyplot(fig)

# Tren Penyewaan Sepeda Berdasarkan Hari
st.subheader("Rata-rata Penyewaan Sepeda per Hari")
daily_rentals = day_df.groupby("weekday")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=daily_rentals.index, y=daily_rentals.values, palette="coolwarm", ax=ax)
plt.xticks(ticks=range(7), labels=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.title("Rata-rata Penyewaan Sepeda per Hari")
st.pyplot(fig)

# Tren Distribusi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=day_df['season'], y=day_df['cnt'], palette='Set2', ax=ax)
plt.xlabel("Musim")
plt.ylabel("Total Penyewaan")
plt.title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("1. Penyewaan sepeda cenderung lebih tinggi pada musim panas dan gugur.")
st.write("2. Cuaca buruk seperti hujan deras atau salju menyebabkan penurunan jumlah penyewaan.")
st.write("3. Penyewaan sepeda paling ramai pada jam 7-9 pagi dan 5-7 sore, bertepatan dengan jam kerja.")
st.write("4. Penyewaan lebih sedikit pada tengah malam hingga subuh.")
st.write("5. Hari kerja memiliki pola penyewaan yang lebih tinggi pada jam sibuk.")
st.write("6. Akhir pekan mungkin memiliki pola penyewaan yang lebih merata sepanjang hari.")
