from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    weight: float
    power: float

    def calculate_damage(self):
        return self.weight * self.power


@dataclass
class Drivetrain:
    name: str
    weight: float
    speed: float

    def calculate_performance(self):
        return self.weight * self.speed


def main():
    weapon = Weapon("Axe", 10.0, 5.0)
    drivetrain = Drivetrain("Wheels", 20.0, 10.0)

    weapon_damage = weapon.calculate_damage()
    drivetrain_performance = drivetrain.calculate_performance()

    print(f"Weapon Damage: {weapon_damage}")
    print(f"Drivetrain Performance: {drivetrain_performance}")


if __name__ == "__main__":
    main()
