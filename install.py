import os
import yaml

import matplotlib as mpl

from templates import MATPLOTLIB_TEMPLATE


def expand_colours(colours):
    '''Expand dict with colours into a list.'''
    expanded_colours = []

    for shade in ['dark', 'light']:
        for colour in colours:
            _, shades = tuple(colour.items())[0]
            expanded_colours.append(shades[shade])

    return expanded_colours


if __name__ == '__main__':
    config_dir = mpl.get_configdir()
    style_dir = os.path.join(config_dir, 'stylelib')

    with open('colours.yaml', 'r') as fh:
        colours = yaml.load(fh.read(), Loader=yaml.Loader)

    expanded_colours = expand_colours(colours)

    if not os.path.exists(style_dir):
        os.makedirs(style_dir)

    with open(os.path.join(style_dir, 'wimm.mplstyle'), 'w') as fh:
        fh.write(MATPLOTLIB_TEMPLATE.format(colours=', '.join([f"'{colour}'" for colour in expanded_colours])))
