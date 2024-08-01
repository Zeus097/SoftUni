from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT = 7

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, self.WEIGHT)

    def eating(self):
        self.weight += 1

