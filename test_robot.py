# File 3: test_robot.py

```python
import unittest
from robot import Robot


class TestRobot(unittest.TestCase):

    def test_robot_info(self):
        robot = Robot()
        robot.set_weight(100)
        robot.set_drive_motors(4)
        robot.set_weapon('Sawblade')
        robot.set_armor('Titanium')
        robot.set_speed(20)
        robot.set_power('Battery')

        expected_output = "Robot Info:\nWeight: 100\nDrive Motors: 4\nWeapon: Sawblade\nArmor: Titanium\nSpeed: 20\nPower: Battery\n"
        self.assertEqual(expected_output, robot.print_robot_info())


if __name__ == '__main__':
    unittest.main()

```