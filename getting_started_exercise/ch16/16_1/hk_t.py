import os
import csv
from datetime import datetime

from matplotlib import pyplot as plt

basedir = os.path.dirname(__file__)
file_max = os.path.join(basedir, 'CLMMAXT_HKO_.csv')
file_min = os.path.join(basedir, 'CLMMINT_HKO_.csv')

with open(file_max, encoding='utf-8') as f_max:
    reader = csv.reader(f_max)

    for n in range(3):
        header_row = next(reader)

    date, max_temps = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(f"{row[0]}-{row[1]}-{row[2]}", "%Y-%m-%d")
            max_temp = int(float(row[3]))
        except (IndexError, ValueError) as e:
            print(f"Error occurred: {e}")
        else:
            max_temps.append(max_temp)
            date.append(current_date)

with open(file_min, encoding='utf-8') as f_min:
    reader = csv.reader(f_min)

    for n in range(3):
        header_row = next(reader)

    min_temps = []
    for row in reader:
        try:
            min_temp = float(row[3])
        except (IndexError, ValueError) as e:
            print(f"Error occurred: {e}")
        else:
            min_temps.append(min_temp)

# Plot date.
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(date, max_temps, alpha=0.5)
plt.plot(date, min_temps, c='red', alpha=0.5)
plt.fill_between(date, max_temps, min_temps, facecolor='blue', alpha=0.1)

# Format plot
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Maximum and Minimum Temperature (°C) at the Hong Kong Observatory')
fig.autofmt_xdate()
plt.tick_params(axis='x', which='major', labelsize=12)
plt.tick_params(axis='y', which='major', labelsize=16)
plt.show()