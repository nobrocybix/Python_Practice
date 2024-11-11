import os
import csv
from datetime import datetime

from matplotlib import pyplot as plt

dir = os.path.dirname(__file__)
file = os.path.join(dir, 'death_valley_2014.csv')

with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for i, r in enumerate(header_row):
        print(i, r)
        
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")            
            high = int(row[4])
            low = int(row[6])
        except ValueError:
            print(current_date, 'missing data')
        else:    
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low Dew Point - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Dew Point", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()