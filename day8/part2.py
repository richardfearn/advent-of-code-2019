#! /usr/bin/python3

import itertools

BLACK = 0
WHITE = 1
TRANSPARENT = 2


class Image:

    def __init__(self, line, width, height):

        self.width = width
        self.height = height
        self.image_size = width * height
        self.pixels = [int(i) for i in line]

        if (len(self.pixels) % self.image_size) > 0:
            raise Exception("Input size (%d) is not a multiple of image size (%d × %d = %d)" %
                            (len(self.pixels), self.width, self.height, self.image_size))

        self.layers = chunks(self.pixels, self.image_size)

    def render(self):
        rendered = []
        for i in range(0, self.image_size):
            pixels = [layer[i] for layer in self.layers]
            actual_colour = next(itertools.dropwhile(lambda x: x == TRANSPARENT, pixels))
            rendered.append(actual_colour)
        return rendered

    def render_as_string(self):
        rendered = self.render()
        rendered = ["██" if x else "  " for x in rendered]
        rendered = chunks(rendered, self.width)
        rendered = ["".join(row) for row in rendered]
        rendered = "\n".join(rendered)
        return rendered


def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
