import random
import math
from Person import Person
from Drawing import DrawController

NUMBEROFPOINTS = 50
FPS = 30
WINDOWHEIGHT = 972
WINDOWWIDTH = 1728
SIGMA = 0.1

people = []

draw = DrawController()
draw.menu_screen()

# for n in range(0, NUMBEROFPOINTS):
# thispoint = Person(random.random(), random.random(), random.random() * 360 - 180)
#     people.append(thispoint)
#
# for person in people:
#     for n in range(0, 5):
#         person.friends.append(random.choice(people))
#
#
# def get_pos(x, y):
#     return (int(x * WINDOWWIDTH), int(y * WINDOWHEIGHT))
#
#
# def gaussian(b, c, x):
#     coefficient = 1.0 / (float(c) * math.sqrt(2 * math.pi))
#     exponential = math.exp(-((float(x) - float(b)) ** 2) / (2 * (float(c) ** 2)))
#     return coefficient * exponential
#
#
# def can_see(x, y, direction, distance=100):
#     visible = []
#     for point in people:
#         direction = (point.x - x, point.y - y)
#         if math.sqrt((point.x - x) ** 2 + (point.y - y) ** 2):
#             if point.y < math.tan(math.radians(point.direction + 10)):
#                 if point.y > math.tan(math.radians(point.direction - 10)):
#                     visible.append(point)
#     return visible
#
#
# loop = True
