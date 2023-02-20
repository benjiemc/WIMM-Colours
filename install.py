import os
import matplotlib as mpl

from templates import MATPLOTLIB_TEMPLATE

config_dir = mpl.get_configdir()
style_dir = os.path.join(config_dir, 'stylelib')

if not os.path.exists(style_dir):
    os.makedirs(style_dir)

with open(os.path.join(style_dir, 'wimm.mplstyle'), 'w') as fh:
    fh.write(MATPLOTLIB_TEMPLATE)
