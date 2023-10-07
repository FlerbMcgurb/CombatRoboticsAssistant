from robot import Robot

class RobotDesign:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot: Robot):
        self.robots.append(robot)

    def get_robot(self, name: str) -> Robot:
        for robot in self.robots:
            if robot.name == name:
                return robot
        return None

    def remove_robot(self, name: str):
        robot = self.get_robot(name)
        if robot:
            self.robots.remove(robot)

    def __str__(self):
        result = ""
        for robot in self.robots:
            result += str(robot) + "\n\n"
        return result
