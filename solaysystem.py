class SolarSystem:
    def __init__(self, name):
        self.name = name

    def show_ss_name(self):
        return f'The only star in our solar system is the {self.name}'


class Planet(SolarSystem):
    def __init__(self, name):
        super().__init__(name)
        self.orbits_a_star = True
        self.mass_enough_to_form_a_sphere = True
        self.cleared_neighborhood_around_orbit = True

    def show_name(self):
        return f'I am planet {self.name}'


class Atm_Moon(Planet):
    def __init__(self, name, atm_type, num_moons):
        super().__init__(name)
        self.moons = num_moons
        self.atmosphere = atm_type

    def show_moons(self):
        return f'I have {self.moons} moons'

    def show_atmosphere(self):
        return f'My atmosphere is mostly {self.atmosphere}'


# Example usage
# P4WAM = Atm_Moon('Mars', 'carbon dioxide', 2)
# print(P4WAM.show_name())
# print(P4WAM.show_moons())
# print(P4WAM.show_atmosphere())

print(Atm_Moon.__dict__)