import csv


class LanternFish:
    init_school = None
    lantern_fish = []
    regen_days = 6

    def __init__(self, _days):
        self.no_of_days = _days
        self.get_school()
        self.update_fish()
        self.print_quantity()

    def get_school(self):
        with open("input.txt", 'r') as input_file:
            self.init_school = list(map(int, list(csv.reader(input_file))[0]))
            self.lantern_fish = self.init_school.copy()

    def add_laternfish(self, _qty):
        for i in range(0, _qty):
            self.lantern_fish.append(8)

    def update_fish(self):
        qty_to_add = 0
        for day in range(0, self.no_of_days):
            print(day)
            for i, fish in enumerate(self.lantern_fish):
                if fish == 0:
                    self.lantern_fish[i] = self.regen_days
                    qty_to_add += 1
                else:
                    self.lantern_fish[i] = fish - 1

            if qty_to_add:
                self.add_laternfish(qty_to_add)

            qty_to_add = 0

    def print_quantity(self):
        print(f"Lantern Fish: {len(self.lantern_fish)}")


school = LanternFish(18)
