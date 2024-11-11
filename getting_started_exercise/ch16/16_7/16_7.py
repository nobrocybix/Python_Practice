import os, csv
import country_codes as cc
import pygal.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

basedir = os.path.dirname(__file__)
filename = os.path.join(basedir, 'GDP.csv')

# Load the data into a list.
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)

    # Read the remaining data.
    for n in range(4):
        header_row = next(reader)
    
    for i, r in enumerate(header_row):
        print(i, r)

    cc_gdp = {}
    for row in reader:
        try:
            country_name = row[3]
            s = row[4].replace(",", "")
            dollars = int(s)

            code = cc.get_country_code(country_name)
            if code:
                cc_gdp[code] = dollars
            else:
                print("missing code:", country_name)

        except ValueError as e:
            pass

    print(len(cc_gdp))
    
wm_style = RS('#45ca71', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Gross domestic product 2023'
wm.add('M of US dollars', cc_gdp)
wm.render_to_file(os.path.join(basedir, 'gdp.svg')) 