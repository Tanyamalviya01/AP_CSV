import csv
from datetime import datetime
import matplotlib.pyplot as plt

# read sitka data first
infile = open('sitka_weather_2018_simple.csv', 'r')
csv_file = csv.reader(infile)
header_row = next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

# find column indexes automatically
date_index = header_row.index('DATE')
tmax_index = header_row.index('TMAX') 
tmin_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

print(f"Date index: {date_index}")
print(f"TMAX index: {tmax_index}")
print(f"TMIN index: {tmin_index}")
print(f"Name index: {name_index}")

sitka_highs = []
sitka_dates = []
sitka_lows = []
sitka_name = ""

for row in csv_file:
    try:
        some_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[tmax_index])
        low = int(row[tmin_index])
        sitka_name = row[name_index]
    except ValueError:
        print(f"Missing data for {row[date_index]}")
    else:
        sitka_highs.append(high)
        sitka_lows.append(low)
        sitka_dates.append(some_date)

infile.close()

print(sitka_highs[:5])
print(sitka_dates[:5])
print("Sitka station name:", sitka_name)

# read death valley data
infile = open('death_valley_2018_simple.csv', 'r')
csv_file = csv.reader(infile)
header_row = next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

# find column indexes automatically for death valley
date_index = header_row.index('DATE')
tmax_index = header_row.index('TMAX')
tmin_index = header_row.index('TMIN') 
name_index = header_row.index('NAME')

dv_highs = []
dv_dates = []
dv_lows = []
dv_name = ""

for row in csv_file:
    try:
        some_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[tmax_index])
        low = int(row[tmin_index])
        dv_name = row[name_index]
    except ValueError:
        print(f"Missing data for {row[date_index]}")
    else:
        dv_highs.append(high)
        dv_lows.append(low)
        dv_dates.append(some_date)

infile.close()

print(dv_highs[:5])
print(dv_dates[:5])
print("Death Valley station name:", dv_name)

# create subplot comparison
fig = plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(sitka_dates, sitka_highs, c="red", alpha=0.5)
plt.plot(sitka_dates, sitka_lows, c="blue", alpha=0.5)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)
plt.title(sitka_name, fontsize=14)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=10)

plt.subplot(2, 1, 2)
plt.plot(dv_dates, dv_highs, c="red", alpha=0.5)
plt.plot(dv_dates, dv_lows, c="blue", alpha=0.5)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)
plt.title(dv_name, fontsize=14)
plt.xlabel("Dates", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=10)

plt.suptitle(f"Temperature comparison between {sitka_name} and {dv_name}", fontsize=16)

fig.autofmt_xdate()
plt.tight_layout()
plt.show()
