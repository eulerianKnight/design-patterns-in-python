from enum import Enum


# Consider a website where a customer can find a product they want to buy.
# A Product can be defined in terms of product name, color, sizes.
# Define a class define enums for product.

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Below is an example of OCP violation
# When the state space increases, the number of methods will increase drastically.
# class BadProductFilter:
#     def filter_by_color(self, products, color):
#         for p in products:
#             if p.color == color: yield p
#
#     def filter_by_size(self, products, size):
#         for p in products:
#             if p.size == size: yield p
#
#     def filter_by_size_and_color(self, products, size, color):
#         for p in products:
#             if p.color == color and p.size == size:
#                 yield p

# Specification
# Use a Base class

class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product()
