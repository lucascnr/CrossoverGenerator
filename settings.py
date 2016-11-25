from os import listdir, path

# Sizes
INPUT_SIZE = (20, 10)
CELL_SIZE = (50, 100)
CENTER_SIZE = (100, 100)
BACKGROUND_SIZE = (600, 600)

# Inputs
INPUTS = (1,0)

# Paths
DIR_PATH = path.dirname(path.realpath(__file__))
CENTER_CELLS_PATH = DIR_PATH + '/center_cells/'
OUTPUT_PATH = DIR_PATH + '/generated_images/'
