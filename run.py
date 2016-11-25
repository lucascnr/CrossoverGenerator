from os import listdir

from settings import CENTER_CELLS_PATH, INPUT_SIZE, CELL_SIZE, CENTER_SIZE
from settings import BACKGROUND_SIZE, INPUTS
from CrossoverDesigner import CrossoverDesigner

crossover = CrossoverDesigner(BACKGROUND_SIZE, CELL_SIZE, INPUT_SIZE,
                              CENTER_SIZE)

for im_name in listdir(CENTER_CELLS_PATH):
    crossover.draw_crossover(INPUTS, im_name, im_name)
