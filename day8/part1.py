#! /usr/bin/python3


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

    def layer_with_fewest_0_digits(self):
        (min_layer_num, min_num_0_digits) = (None, None)
        for (layer_num, layer) in enumerate(self.layers):
            num_0_digits = layer.count(0)
            if (min_num_0_digits is None) or (num_0_digits < min_num_0_digits):
                (min_layer_num, min_num_0_digits) = (layer_num, num_0_digits)
        return min_layer_num


def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
