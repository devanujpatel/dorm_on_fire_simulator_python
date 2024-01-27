import random
import time
from vertices_and_edges import VerticesAndEdges
class Fire:
    def __init__(self, input_fire_tiles, all_tiles_list, all_tiles_dict):
        self.fireTiles = input_fire_tiles
        self.all_tiles_list = all_tiles_list
        self.all_tiles_dict = all_tiles_dict
        self.dataset = VerticesAndEdges(self.all_tiles_list, self.all_tiles_dict)


    # Method to start the fire simulation
    def start_fire(self):
        print("Fire simulation started.")

    # Method to spread the fire based on factors
    def spread_fire(self):
        time.sleep(5)
        x = self.x
        y = self.y
        # top left cell
        if x - 1 >= 0 and y - 1 >= 0 and self.all_tiles_dict[x - 1][y - 1] is not None and self.all_tiles_dict[x - 1][
            y - 1].flammable == True:
            self.all_tiles_dict[x - 1][y - 1].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x - 1][y - 1])

            # top up same column
        if y - 1 >= 0 and self.all_tiles_dict[x][y - 1] is not None and self.all_tiles_dict[x][y - 1].flammable == True:
            self.all_tiles_dict[x][y - 1].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x][y - 1])

            # top right
        if x + 1 <= 99 and y - 1 >= 0 and self.all_tiles_dict[x - 1][y - 1] is not None and self.all_tiles_dict[x - 1][
            y - 1].flammable == True:
            self.all_tiles_dict[x - 1][y - 1].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x - 1][y - 1])

            # same level left
        if x - 1 >= 0 and self.all_tiles_dict[x - 1][y] is not None and self.all_tiles_dict[x - 1][y].flammable == True:
            self.all_tiles_dict[x - 1][y].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x - 1][y])

            # same level right
        if x + 1 <= 99 and self.all_tiles_dict[x + 1][y] is not None and self.all_tiles_dict[x + 1][y].flammable == True:
            self.all_tiles_dict[x + 1][y].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x + 1][y])

            # bottom left
        if x - 1 >= 0 and y + 1 <= 99 and self.all_tiles_dict[x - 1][y + 1] is not None and self.all_tiles_dict[x - 1][
            y + 1].flammable == True:
            self.all_tiles_dict[x - 1][y + 1].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x - 1][y + 1])

        # same column bottom down
        if y + 1 <= 99 and self.all_tiles_dict[x][y + 1] is not None and self.all_tiles_dict[x][y + 1].flammable == True:
            self.all_tiles_dict[x][y + 1].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x][y + 1])

        # bottom right
        if x + 1 <= 99 and y + 1 <= 99 and self.all_tiles_dict[x + 1][y + 1] is not None and self.all_tiles_dict[x + 1][
            y + 1].flammable == True:
            self.all_tiles_dict[x + 1][y + 1].set_on_fire()
            self.input_fire_tiles.append(self.all_tiles_dict[x + 1][y + 1])

        self.input_fire_tiles.pop(0)
        self.input_fire_tiles[0].spread_fire()


    # Method to consume building material
    def consume_material(self, material):
        # Simulate material consumption based on the type of material
        print(f"Fire is consuming {material}")

    # Method to generate smoke
    def generate_smoke(self):
        # Simulate smoke generation
        print("Smoke is generated.")

    # Method to increase fire intensity
    def intensity_increase(self):
        self.intensity += 5  # Simulate a gradual increase in intensity
        print(f"Fire intensity increased to {self.intensity}")

    # Method to check for firefighters
    def check_firefighters(self):
        if self.intensity > 15:
            print("Firefighters are on the scene.")

    # Method to simulate extinguishing efforts
    def simulate_extinguishing_efforts(self):
        if self.sprinkler_system_active:
            self.intensity -= 8  # Simulate the effect of the sprinkler system
            print("Sprinkler system is active. Fire intensity reduced.")

    # Method to calculate and simulate structural damage
    def structural_damage(self):
        if self.intensity > 20:
            print("Structural damage occurred.")

    # Method to detect fire alarms
    def detect_fire_alarms(self):
        if self.intensity > 10:
            self.fire_alarm_activated = True
            print("Fire alarm activated.")

    # Method to simulate building evacuation
    def evacuate_building(self):
        if self.intensity > 25:
            print("Evacuating the building.")

    # Method to get simulation status
    def get_simulation_status(self):
        print(f"Simulation Status - Intensity: {self.intensity}, "
              f"Sprinkler System: {'Active' if self.sprinkler_system_active else 'Inactive'}, "
              f"Fire Alarm: {'Activated' if self.fire_alarm_activated else 'Deactivated'}")

    # Method to activate the sprinkler system
    def activate_sprinkler_system(self):
        self.sprinkler_system_active = True
        print("Sprinkler system activated.")

    # Method to deactivate the sprinkler system
    def deactivate_sprinkler_system(self):
        self.sprinkler_system_active = False
        print("Sprinkler system deactivated.")

    # Method to adjust sprinkler intensity
    def adjust_sprinkler_intensity(self, intensity):
        print(f"Sprinkler intensity adjusted to {intensity}")

    # Method to simulate the effect of wind on fire spread
    def simulate_fire_spread_with_wind(self, wind_speed):
        self.intensity += wind_speed // 2
        print(f"Wind is affecting fire spread. Intensity: {self.intensity}")

    # Method to simulate the effect of ventilation systems on fire spread
    def simulate_fire_spread_with_ventilation(self, ventilation_on):
        if ventilation_on:
            self.intensity -= 3
            print("Ventilation is reducing fire intensity.")

    # Method to simulate the effect of different fuel types on fire behavior
    def simulate_fire_spread_with_fuel_type(self, fuel_type):
        if fuel_type.lower() == "flammable":
            self.intensity += 10
            print("Flammable fuel is increasing fire intensity.")
        elif fuel_type.lower() == "nonflammable":
            self.intensity -= 5
            print("Nonflammable fuel is reducing fire intensity.")
        else:
            print("Unknown fuel type. No significant impact on fire intensity.")

    # Method to simulate the effect of temperature on fire behavior
    def simulate_fire_spread_with_temperature(self, temperature):
        self.intensity += temperature // 3
        print(f"Temperature is affecting fire spread. Intensity: {self.intensity}")

    # Method to simulate the effect of oxygen levels on fire intensity
    def simulate_fire_spread_with_oxygen_level(self, oxygen_level):
        self.intensity += oxygen_level // 2
        print(f"Oxygen level is affecting fire intensity. Intensity: {self.intensity}")

    # Method to simulate the effect of humidity on fire behavior
    def simulate_fire_spread_with_humidity(self, humidity):
        self.intensity -= humidity // 4
        print(f"Humidity is reducing fire intensity. Intensity: {self.intensity}")

    # Method to simulate the impact of building layout on fire spread
    def simulate_fire_spread_with_building_layout(self, building_layout):
        if building_layout.lower() == "open":
            self.intensity -= 3
            print("Open building layout is reducing fire intensity.")
        elif building_layout.lower() == "closed":
            self.intensity += 5
            print("Closed building layout is increasing fire intensity.")
        else:
            print("Unknown building layout. No significant impact on fire intensity.")

    # Method to simulate the impact of different occupancies on fire behavior
    def simulate_fire_spread_with_occupancy(self, occupancy_type):
        if occupancy_type.lower() == "residential":
            self.intensity += 8
            print("Residential occupancy is increasing fire intensity.")
        elif occupancy_type.lower() == "commercial":
            self.intensity += 5
            print("Commercial occupancy is increasing fire intensity.")
        else:
            print("Unknown occupancy type. No significant impact on fire intensity.")

    # Method to simulate the presence of firebreaks affecting fire spread
    def simulate_fire_spread_with_firebreaks(self, firebreaks_present):
        if firebreaks_present:
            self.intensity -= 6
            print("Firebreaks are reducing fire intensity.")
        else:
            print("No firebreaks present. No significant impact on fire intensity.")

    # Method to simulate the impact of firefighters on fire spread
    def simulate_fire_spread_with_firefighters_on_scene(self, firefighters_present):
        if firefighters_present:
            self.intensity -= 10
            print("Firefighters on the scene are reducing fire intensity.")
        else:
            print("No firefighters present. No significant impact on fire intensity.")

    # Method to simulate the effect of fire retardant on fire intensity
    def simulate_fire_spread_with_retardant(self, fire_retardant_present):
        if fire_retardant_present:
            self.intensity -= 12
            print("Fire retardant is significantly reducing fire intensity.")
        else:
            print("No fire retardant present. No significant impact on fire intensity.")

    # Method to simulate the use of fire extinguishers
    def simulate_fire_spread_with_extinguisher_use(self, extinguisher_used):
        if extinguisher_used:
            self.intensity -= 15
            print("Fire extinguisher used. Fire intensity significantly reduced.")
        else:
            print("No fire extinguisher used. No significant impact on fire intensity.")

    # Method to calculate the overall risk level for building occupants
    def calculate_risk_level(self):
        risk = self.intensity

        if self.fire_alarm_activated:
            risk -= 5

        if self.sprinkler_system_active:
            risk -= 3

        return risk

    # Method to provide information on suggested escape routes based on risk level
    def suggest_escape_route(self, risk_level):
        if risk_level > 15:
            print("High risk level! Consider alternative escape routes.")
        else:
            print("Low to moderate risk. Standard escape routes can be used.")

    # Method to calculate visibility due to smoke
    def calculate_visibility(self):
        visibility = random.randint(0, 100)  # Simulate random visibility value

        if visibility < 30:
            print("Low visibility due to smoke. Use caution.")
        else:
            print("Visibility is acceptable.")

    # Method to simulate changes in fire behavior over time
    def simulate_fire_behavior_change_over_time(self):
        time_factor = random.randint(-1, 1)  # Simulate random time factor (-1, 0, 1)
        self.intensity += time_factor * 5  # Adjust intensity based on time factor
        print(f"Fire behavior is changing over time. Intensity: {self.intensity}")

    # Method to simulate the impact of various building materials on fire spread
    def simulate_fire_spread_with_building_materials(self, materials):
        for material in materials:
            if material.lower() == "flammable":
                self.intensity += 7
                print("Flammable material is increasing fire intensity.")
            elif material.lower() == "nonflammable":
                self.intensity -= 4
                print("Nonflammable material is reducing fire intensity.")
            else:
                print("Unknown building material. No significant impact on fire intensity.")
