class My_dimension(model.Dimension):

    attributes = list()
    dimension_name = str()

    degree = 0.0

    def __init__(self, dimension_name):
        self.dimension_name = dimension_name

    def get_attributes(self);
        return self.attributes

    def get_dimension_name(self):
        return self.dimension_name

    def dimension_degree(self):
        for x in attributes:
            self.degree += x

        return self.degree
