# File 2: robot.py

```python

class Robot:
    def __init__(self):
        self.weight = None
        self.drive_motors = None
        self.weapon = None
        self.armor = None
        self.speed = None
        self.power = None

    def set_weight(self, weight):
        self.weight = weight

    def set_drive_motors(self, drive_motors):
        self.drive_motors = drive_motors

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_armor(self, armor):
        self.armor = armor

    def set_speed(self, speed):
        self.speed = speed

    def set_power(self, power):
        self.power = power

    def print_robot_info(self):
        print("Robot Info:")
        print(f"Weight: {self.weight}")
        print(f"Drive Motors: {self.drive_motors}")
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"Speed: {self.speed}")
        print(f"Power: {self.power}")

```