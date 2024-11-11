import os
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'death_valley_2014.csv')
filename2 = os.path.join(dir, 'sitka_weather_2014.csv')
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates2, highs2, lows2 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates2.append(current_date)
            highs2.append(high)
            lows2.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates2, highs2, c='#e0d117', alpha=0.5)
plt.plot(dates2, lows2, c='#e05417', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.fill_between(dates2, highs2, lows2, facecolor='#e05417', alpha=0.2)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA and Sitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16,)
plt.tick_params(axis='x', which='major', labelsize=16)
plt.tick_params(axis='y', which='major', labelsize=8)

plt.show()
