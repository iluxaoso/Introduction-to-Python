import csv
import os


class CarBase:
    car_type = ""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            self.carrying = 0.0

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self.passenger_seats_count = 0


class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)

        try:
            body_whl = body_whl.split("x")
            self.body_length = float(body_whl[0])
            self.body_width = float(body_whl[1])
            self.body_height = float(body_whl[2])
            if self.body_length == 0.0 or self.body_width == 0.0 or self.body_height == 0.0 or len(body_whl) != 3:
                self.body_length = 0.0
                self.body_width = 0.0
                self.body_height = 0.0
        except ValueError:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def check_data(row):
    if len(row) == 7:
        if row[0] != "" and row[1] != "" and row[3] != "" and row[5] != "" \
             and row[0] is not None and row[1] is not None and row[3] is not None and row[5] is not None:
            car_base = CarBase(row[1], row[3], row[5])
            try:
                ext = car_base.get_photo_file_ext()
                if ext != ".jpg" and ext != ".jpeg" and ext != ".png" and ext != ".gif":
                    return False
                else:
                    return True
            except IndexError:
                pass

            try:
                car_base.carrying = float(car_base.carrying)
            except ValueError:
                return False
            return True
        else:
            return False
    else:
        return False


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename, "r") as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                if check_data(row):
                    print(row)
                    if row[0] == "car" and row[2] != "" and row[4] == "" and row[6] == "":
                        car_list.append(Car(row[1], row[3], row[5], row[2]))
                    elif row[0] == "truck" and row[2] == "" and row[6] == "":
                        car_list.append(Truck(row[1], row[3], row[5], row[4]))
                    elif row[0] == "spec_machine" and row[2] == "" and row[4] == "" and row[6] != "":
                        car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
        return car_list
    except FileNotFoundError:
        pass
