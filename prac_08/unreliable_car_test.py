from unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar("New car", 100, 80)
    old_car = UnreliableCar("Old car", 100, 20)

    for i in range(10):
        new_car.drive(10)
        old_car.drive(10)

    print(new_car)
    print(old_car)


main()
