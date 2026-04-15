# ===============================
# 1. Import Libraries
# ===============================
# نستورد المكتبات الي نحتاجها عشان تحليل البيانات والرسم

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Libraries imported successfully")


# ===============================
# 2. Load Dataset
# ===============================
#عشان نقدر نقراء البيانات الي برابط البيانات حقنا pandas نستخدم

url = "https://rcs.bu.edu/examples/python/DataAnalysis/flights.csv"
df = pd.read_csv(url)


# ===============================
# 3. Explore the Dataset
# ===============================
# نعرض اول 10 صفوف من البيانات عشان نعرف شكل البيانات ونشوف الاعمده الي فيها

print(df.head(10))

# يعرض شكل البيانات (عدد الصفوف والاعمده )   
print("Shape of dataset:")
print(df.shape)

# يعرض اسماء الاعمده 
print("\nColumn names:")
print(df.columns)

#  يعرض معلومات بشكل عام عن البيانات مثل نوع البيانات وعدد القيم غير المفقوده في كل عمود
print("\nDataset information:")
print(df.info())


# ===============================
# 4. Check Missing Values
# ===============================
# يحسب عدد القيم المفقوده في كل عمود

print("\nMissing values in each column:")
print(df.isnull().sum())


# ===============================
# 5. Data Cleaning
# ===============================
# عشان نعالج القيم المفقوده في عمود تأخير المغادره و تأخير الوصول نقدر نعوضهم ب 0 لان اذا كان الطياره ما اتأخرت معناته التأخير يساوي صفر
df['dep_delay'] = df['dep_delay'].fillna(0)
df['arr_delay'] = df['arr_delay'].fillna(0)


# يعرض حجم البيانات قبل التنظيف
print("\nDataset shape before cleaning:")
print(df.shape)

# نحذف القيم المفقوده في عامود وقت الرحله عشان نقدر نستخدمه في التحليل والرسم لان اذا كان فيه قيم مفقوده في هذا العامود ممكن ياثر على النتائج
df_clean = df.dropna(subset=['air_time'])

# يعرض حجم البيانات بعد التنظيف
print("\nDataset shape after removing missing values:")
print(df_clean.shape)


# ===============================
# 6. Descriptive Statistics
# ===============================
# نحسب بعض الاحصائيات الوصفية لتأخير المغادره وتأخير الوصول مثل المتوسط والوسيط والانحراف المعياري
print("\nDescriptive Statistics:")

print("\nDeparture Delay:")
print("Mean:", df_clean['dep_delay'].mean())
print("Median:", df_clean['dep_delay'].median())
print("Standard Deviation:", df_clean['dep_delay'].std())

print("\nArrival Delay:")
print("Mean:", df_clean['arr_delay'].mean())
print("Median:", df_clean['arr_delay'].median())
print("Standard Deviation:", df_clean['arr_delay'].std())

# نحدد الرحله الي قطعت اطول مسافه والرحله الي قطعت اقصر مسافه
longest_flight = df_clean.loc[df_clean['distance'].idxmax()]
shortest_flight = df_clean.loc[df_clean['distance'].idxmin()]

print("\nFlight with longest distance:")
print(longest_flight)

print("\nFlight with shortest distance:")
print(shortest_flight)


# ===============================
# 7. Grouping Analysis
# ===============================
# نحسب متوسط تأخير الاقلاع والوصول لكل شركة طيران

carrier_stats = df_clean.groupby('carrier')[['dep_delay', 'arr_delay']].mean()

print("\nAverage departure and arrival delay by carrier:")
print(carrier_stats)

# نحسب عدد الرحلات والمسافه الاجماليه لكل مطار مغادره
origin_stats = df_clean.groupby('origin').agg({
    'flight': 'count',
    'distance': 'sum'
})

print("\nTotal number of flights and total distance by origin airport:")
print(origin_stats)


# ===============================
# 8. Visualization Style
# ===============================
#حاجه اختياريه لو نبي نخلي رسوماتنا تطلع بشكل افضل نقدر نختار الستايل الي يعجبنا 

plt.style.use('seaborn-v0_8')


# ===============================
# 9. Average Delay by Airline
# ===============================
# نحسب متوسط تأخير الوصول لكل شركة طيران

carrier_delay = df_clean.groupby('carrier')['arr_delay'].mean()


# ===============================
# 10. Plot Average Delay by Airline
# ===============================
# عشان نرسم متوسط تأخير الوصول لكل شركة طيران Bar chart استخدمنا     

plt.figure(figsize=(8,5))

ax = carrier_delay.plot(kind='bar', color="#735373", edgecolor='black')

plt.title("Average Arrival Delay by Airline")
plt.xlabel("Airline Carrier")
plt.ylabel("Average Arrival Delay (minutes)")

#  حاجه اختياريه ضفنا خطوط شبكه عشان تكون الرسمه والقيم الي فيها اوضح
plt.grid(axis='y', linestyle='--', alpha=0.7)

# حاجه اختياريه ضفنا القيم حقت كل عامود فوقه عشان تكون الرسمه اوضح
# القيمه السالبه صارت داخل العامود بس عادي لانها واضحه
for i, v in enumerate(carrier_delay):
    ax.text(i, v + 0.2, round(v,2), ha='center')

plt.savefig("average_delay_by_airline.png")  # نحفظ الرسمه كصوره
plt.show()


# ===============================
# 11. Number of Flights per Month
# ===============================
# نحسب عدد الرحلات في كل شهر

flights_per_month = df_clean.groupby('month')['flight'].count()

# عشان نوضح عدد الرحلات في كل شهر Line chart استخدمنا
plt.figure(figsize=(8,5))

flights_per_month.plot(kind='line', marker='o', color="#735373")

plt.title("Number of Flights per Month")
plt.xlabel("Month")
plt.ylabel("Number of Flights")

plt.grid(True)

plt.savefig("flights_per_month.png") # نحفظ الرسمه كصوره
plt.show()


# ===============================
# 12. Departure Delay Distribution
# ===============================
# عشان نشوف توزيع تأخير المغادره Histogram استخدمنا

plt.figure(figsize=(8,5))

plt.hist(df_clean['dep_delay'], bins=50, color="#735373", edgecolor='black', alpha=0.8)

plt.title("Distribution of Departure Delays")
plt.xlabel("Departure Delay (minutes)")
plt.ylabel("Number of Flights")

plt.savefig("departure_delay_distribution.png") # نحفظ الرسمه كصوره
plt.show()


# ===============================
# 13. Distance vs Arrival Delay
# ===============================
# عشان نشوف العلاقه بين المسافه وتأخير الوصول Scatter plot استخدمنا

plt.figure(figsize=(8,5))

plt.scatter(df_clean['distance'], df_clean['arr_delay'], color="#735373", alpha=0.4)

plt.title("Distance vs Arrival Delay")
plt.xlabel("Distance (miles)")
plt.ylabel("Arrival Delay (minutes)")

plt.savefig("distance_vs_delay.png")  # نحفظ الرسمه كصوره
plt.show()

