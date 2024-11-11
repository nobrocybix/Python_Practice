import os
import csv
from datetime import datetime

from matplotlib import pyplot as plt

basedir = os.path.dirname(__file__)
file = os.path.join(basedir, 'daily_HKO_RH_2024.csv')

with open(file, encoding="utf-8") as f:
    reader = csv.reader(f)
    for n in range(3):
        header_row = next(reader) 

    for i, n in enumerate(header_row):
        print(i, n)

    dates, values = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(f"{row[0]}-{row[1]}-{row[2]}", "%Y-%m-%d")
            value = row[3]
        except (IndexError, ValueError) as e:
            print(f"Error occurred: {e}")
        else:
            values.append(value)
            dates.append(current_date)

# Plot date.
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dates, values)

# Format plot
plt.xlabel('Date', fontsize=16)
plt.ylabel('Value', fontsize=16)
plt.title('Daily Mean Relative Humidity (%) at the Hong Kong Observatory')
fig.autofmt_xdate()
plt.tick_params(axis='x', which='major', labelsize=12)
plt.tick_params(axis='y', which='major', labelsize=8)
plt.show()