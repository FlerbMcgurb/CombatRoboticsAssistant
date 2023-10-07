# File 1: main.py

```python
from robot import Robot


def main():
    robot = Robot()
    robot.set_weight(100)
    robot.set_drive_motors(4)
    robot.set_weapon("Spinner")
    robot.set_armor("Steel")
    robot.set_speed(10)
    robot.set_power(100)
    robot.print_robot_info()


if __name__ == "__main__":
    main()
```