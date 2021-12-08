import csv


class LanternFish:
    init_school = None
    lantern_fish = []
    regen_days = 6
    age = None

    def __init__(self, _days):
        self.no_of_days = _days
        self.get_school()
        self.group_by_age()
        self.update_age()

    def get_school(self):
        with open("input.txt", 'r') as input_file:
            self.init_school = list(map(int, list(csv.reader(input_file))[0]))
            self.lantern_fish = self.init_school.copy()

    def add_laternfish(self, _qty):
        for i in range(0, _qty):
            self.lantern_fish.append(8)

    def group_by_age(self):
        self.age = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
        for age in self.lantern_fish:
            self.age[str(age)] += 1

    def update_age(self):
        fish_to_add = 0
        for day in range(0, self.no_of_days):
            for age in self.age:
                if age == '0':
                    fish_to_add = self.age['0']
                else:
                    self.age[str(int(age)-1)] = self.age[age]

            if fish_to_add > 0:
                self.age['8'] = fish_to_add
                self.age['6'] += fish_to_add
                fish_to_add = 0
            else:
                self.age['8'] = 0

        self.print_quantity()

    def print_quantity(self):
        number_of_fish = 0
        for age_group in self.age:
            number_of_fish += self.age[age_group]

        print(number_of_fish)


school = LanternFish(256)
