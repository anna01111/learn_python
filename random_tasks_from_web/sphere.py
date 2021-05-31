from math import pi


class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'rad: {self.radius}, x: {self.x}, y: {self.y}, z: {self.z}'

    def get_volume(self):
        v = 4 / 3 * pi * self.radius ** 3
        return v

    def get_square(self):
        sq = 4 * pi * self.radius ** 2
        return sq

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        x_is_inside = self.x - self.radius <= x <= self.x + self.radius
        y_is_inside = self.y - self.radius <= y <= self.y + self.radius
        z_is_inside = self.z - self.radius <= z <= self.z + self.radius
        return x_is_inside and y_is_inside and z_is_inside


s = Sphere(5, 1, 1, 1)
s2 = Sphere()
s3 = Sphere(10)


# print('volume: ', s.get_volume())
# print('square: ', s.get_square())
# print('radius: ', s.get_radius())
# print('center: ', s.get_center())
#
# s.set_radius(10)
# print('new radius: ', s.get_radius())
#
# print('is inside: ', s.is_point_inside(-9, 0, 2))
#
#
# s.set_center(2, 2, 4)
# print('new center: ', s.get_center())
#
# print('is inside: ', s.is_point_inside(-9, 0, 2))


s0 = Sphere(0.5)  # test sphere creation with radius and default center
print(s0.get_center())  # (0.0, 0.0, 0.0)
print(s0.get_volume())  # 0.523598775598
print(s0.is_point_inside(0, -1.5, 0))  # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))  # True
print(s0.get_radius())  # 1.6

