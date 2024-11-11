import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

basedir = os.path.dirname(__file__)
filename = os.path.join(basedir, 'greenhouse_gas_emissions_and_carbon_intensity.json')

# Load the data into a list.
with open(filename) as f:
    datas = json.load(f)

d, y = [], []

for data in datas:
    Report_Year = datetime.strptime(data['Report_Year'], "%Y")
    Total_GHG_emissions =  int(float(data['Total_GHG_emissions']))

    d.append(Total_GHG_emissions)
    y.append(Report_Year)

title = "Greenhouse gas emissions 1990-2022"

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(y, d, linewidth=5, c='red')
plt.title(title, fontsize=20)
plt.xlabel("Year", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Total GHG emissions", fontsize=16)
plt.tick_params(axis='both', labelsize=14)
plt.show()