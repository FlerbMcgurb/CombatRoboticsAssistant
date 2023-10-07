from robot import Robot
from robot_design import RobotDesign

def test_robot_design():
    design = RobotDesign()

    robot1 = Robot("Robot 1", 50.0, "Saw", "Steel")
    robot2 = Robot("Robot 2", 40.0, "Hammer", "Aluminum")

    design.add_robot(robot1)
    design.add_robot(robot2)

    assert str(design) == "Name: Robot 1\nWeight: 50.0\nWeapon: Saw\nArmor: Steel\n\nName: Robot 2\nWeight: 40.0\nWeapon: Hammer\nArmor: Aluminum\n\n"

    design.remove_robot("Robot 1")

    assert str(design) == "Name: Robot 2\nWeight: 40.0\nWeapon: Hammer\nArmor: Aluminum\n\n"
