import time

from PIL import Image, ImageDraw
from settings import CENTER_CELLS_PATH, OUTPUT_PATH

class CrossoverDesigner:
    def __init__(self, image_size, rec_size, rec_tiny_size, center_size):
        self.image = Image.new('L', image_size, 'white')
        self.rec_size = rec_size
        self.rec_tiny_size = rec_tiny_size
        self.center_size = center_size

    def _draw(self, start_point, tiny=False):
        size = self.rec_tiny_size if tiny else self.rec_size
        x, y = start_point
        x1, y1 = size

        ImageDraw.Draw(self.image).rectangle((x, y, x + x1, y + y1), fill=0)

    def draw_inputs(self, inputs):
        def get_starter_point(input_number, input_value):
            width = 0

            if input_number == 1:
                if input_value:
                    width = self.rec_size[1] + self.rec_tiny_size[1]

            else:
                width = self.rec_size[1] + self.center_size[1]

                if input_value:
                    width += self.rec_size[1] + self.rec_tiny_size[1]

            return (0, width)

        in1, in2 = inputs

        self._draw(get_starter_point(1, in1), True)
        self._draw(get_starter_point(2, in2), True)

    def draw_wires(self):
        def get_starter_point(rec_position):
            posX, posY = rec_position
            height, width = self.rec_tiny_size

            if posY:
                width += self.rec_size[1] + self.center_size[1]

            if posX:
                height += self.rec_size[0] + self.center_size[0]

            return (height, width)

        for i in range(2):
            for j in range(2):
                self._draw(get_starter_point((i, j)))

    def draw_center_image(self, image_name):
        center_im = Image.open(CENTER_CELLS_PATH + image_name)
        height = self.rec_tiny_size[0] + self.rec_size[0]
        width = self.rec_tiny_size[1] + self.rec_size[1]

        center_im.thumbnail(self.center_size, Image.ANTIALIAS)
        self.image.paste(center_im, (height, width))

    def draw_crossover(self, inputs, center_im_name, output_name):
        self.draw_inputs(inputs)
        self.draw_center_image(center_im_name)
        self.draw_wires()

        self.image.save(OUTPUT_PATH + output_name, 'PNG')
