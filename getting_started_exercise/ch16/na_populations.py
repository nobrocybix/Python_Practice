import pygal.maps
import os

basedir = os.path.dirname(__file__)

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file(os.path.join(basedir, 'na_populations.svg'))