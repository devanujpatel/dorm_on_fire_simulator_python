import heapq

class Person:
    def __init__(self, name, personal_traits=None, position=(0,0)):
        self.name = name
        self.location = None
        self.status = "Inside"
        self.health_status = 100
        self.evacuation_status = False
        self.position = position
        self.blocked_exits = []

    def makeNextMove():
        try:
            # Get the current working directory
            current_directory = os.getcwd()

            dat_files = glob.glob(os.path.join(current_directory, '*.dat'))
            dat_file_names = [os.path.basename(file) for file in dat_files]
            print(dat_file_names)
            var_options = dat_file_names
        except Exception as e:
            print(f"Error: {e}")
        allPossibilities = vertices_and_edges()

    def enter_building(self, entry_point):
        self.location = entry_point
        self.status = "Inside"
        print(f"{self.name} entered the building through {entry_point}.")

    def leave_building(self, exit_point):
        self.location = exit_point
        self.status = "Outside"
        self.evacuation_status = True
        print(f"{self.name} left the building through {exit_point}.")

    def move_to_location(self, new_location):
        self.location = new_location
        print(f"{self.name} moved to {new_location}.")

    def react_to_emergency(self, emergency_type):
        if "panic" in self.personal_traits:
            self.panic_reaction()
        if "heroic" in self.personal_traits:
            self.heroic_reaction()
        print(f"{self.name} reacted to the emergency ({emergency_type}).")

    def panic_reaction(self):
        if random.random() < 0.3:  # 30% chance of panic
            print(f"{self.name} is in a state of panic. Encourage calm communication.")

    def heroic_reaction(self):
        if random.random() < 0.2:  # 20% chance of heroic action
            print(f"{self.name} is acting heroically. Ensure their safety.")

    def guide_in_smoke(self):
        if "reduce_visibility" in self.personal_traits:
            print(f"{self.name} is having difficulty due to reduced visibility. Provide guidance.")

    def provide_assistance(self):
        if "reduced_mobility" in self.personal_traits:
            print(f"{self.name} has reduced mobility. Offer assistance.")

    def follow_instructions(self, instructions):
        if random.random() < 0.5:  # 50% chance of following instructions
            print(f"{self.name} is following instructions: {instructions}.")
        else:
            print(f"{self.name} may not be familiar with the instructions.")

    def assist_vulnerable_individual(self, individual):
        if individual in ["children", "older_adults", "people_with_disabilities"]:
            print(f"{self.name} is assisting {individual} during evacuation.")

    def prioritize_self_preservation(self):
        print(f"{self.name} prioritizes their own safety.")

    def share_information(self, information):
        print(f"{self.name} shares information: {information}.")

    def simulate_fire_drill(self):
        if random.random() < 0.7:  # 70% chance of participating in a fire drill
            print(f"{self.name} is participating in a fire drill. Practice evacuation procedures.")
        else:
            print(f"{self.name} may not be participating in the fire drill.")

    def use_mobile_phone(self):
        if self.mobile_phone_dependence and random.random() < 0.5:  # 50% chance of using the phone
            print(f"{self.name} is using their mobile phone. Encourage responsible use during emergencies.")

    def check_social_media(self):
        if random.random() < 0.3:  # 30% chance of checking social media during an emergency
            print(f"{self.name} is checking social media. Ensure official channels for information.")

    def test_building_alarm_system(self):
        if random.random() < 0.8:  # 80% chance of testing the building alarm system during a drill
            print(f"{self.name} is testing the building alarm system. Ensure it is functional.")

    def provide_alternative_evacuation_plan(self):
        if "disability" in self.personal_traits:
            print(f"{self.name} has a disability. Provide alternative evacuation plans and resources.")

    def offer_multilingual_instructions(self):
        if random.random() < 0.6:  # 60% chance of needing multilingual instructions
            print(f"{self.name} may have a language barrier. Offer instructions in multiple languages.")

    def consider_cultural_background(self):
        if self.cultural_background:
            print(f"{self.name} has a cultural background. Consider cultural factors in communication.")

    def consider_weather_conditions(self, weather_condition):
        if weather_condition in ["heavy_rain", "heavy_snow"]:
            print(f"{self.name} is facing {weather_condition}. Consider alternative plans for extreme weather.")

    def communicate_construction_changes(self, construction_changes):
        if construction_changes:
            print(f"{self.name} is aware of construction changes. Clearly communicate any alterations.")

    def stay_low_in_limited_visibility(self):
        if "limited_visibility" in self.personal_traits:
            print(f"{self.name} is facing limited visibility. Emphasize staying low during evacuation.")

    def offer_mental_health_support(self):
        if "stress" in self.personal_traits or "past_trauma" in self.personal_traits:
            print(f"{self.name} may be experiencing stress or past trauma. Offer mental health support.")
        def navigate_communal_spaces(self):
            if "communal_living" in self.personal_traits:
                print(f"{self.name} is in a communal living space. Be aware of additional fuel sources and evacuation challenges.")

    def enforce_occupancy_limits(self):
        if "overcrowding" in self.personal_traits:
            print(f"{self.name} is in a crowded area. Enforce occupancy limits and implement crowd control measures.")

    def conduct_fire_risk_assessment(self):
        if "non_standard_construction" in self.personal_traits:
            print(f"{self.name} is in a dorm with non-standard construction. Conduct thorough fire risk assessments.")

    def promote_fire_safety_education(self):
        if "unintentional_triggers" in self.personal_traits:
            print(f"{self.name} is engaging in activities with unintentional fire triggers. Promote fire safety education.")

    def address_substance_use(self):
        if "substance_use" in self.personal_traits:
            print(f"{self.name} may be under the influence. Address substance use for fire safety.")

    def emphasize_seriousness_of_fire_safety(self):
        if "prank_behavior" in self.personal_traits:
            print(f"{self.name} is engaging in prank behavior. Emphasize the seriousness of fire safety and enforce discipline.")

    def remain_flexible_and_resourceful(self):
        if "blocked_exits" in self.personal_traits:
            print(f"{self.name} is facing blocked exits. Remain flexible, identify alternative routes, and create safe havens.")

    def navigate_carefully_under_falling_debris(self):
        if "falling_debris" in self.personal_traits:
            print(f"{self.name} is navigating under falling debris. Stay low and be aware of surroundings.")

    def be_cautious_of_hidden_fire_hazards(self):
        if "hidden_fire" in self.personal_traits:
            print(f"{self.name} is cautious of hidden fire hazards. Alert responders to potential risks.")

    def anticipate_erratic_behavior(self):
        if "fight_or_flight" in self.personal_traits:
            print(f"{self.name} may exhibit fight-or-flight responses. Anticipate erratic behavior and guide calmly.")

    def anticipate_panic_and_disorientation(self):
        if "limited_visibility" in self.personal_traits:
            print(f"{self.name} is experiencing limited visibility. Expect panic and disorientation.")

    def anticipate_heightened_anxiety(self):
        if "sound" in self.personal_traits:
            print(f"{self.name} is exposed to loud sounds. Anticipate heightened anxiety and hindered communication.")

    def anticipate_impairment_due_to_smoke_smell(self):
        if "smell" in self.personal_traits:
            print(f"{self.name} is experiencing the pungent smell of smoke. Anticipate impairment in movement and decision-making.")

        def respond_to_clear_alarm(self):
            if random.random() < 0.8:  # 80% chance of responding to a clear and recognizable alarm
                print(f"{self.name} hears a clear and recognizable alarm. Responds promptly.")

    def know_escape_routes(self):
        if "knowledge_of_routes" in self.personal_traits:
            print(f"{self.name} is familiar with escape routes. Moves efficiently towards exits.")

    def experience_panic_and_disorientation(self):
        if "limited_visibility" in self.personal_traits:
            print(f"{self.name} is experiencing limited visibility. May hesitate or feel disoriented.")

    def provide_leadership_and_guidance(self):
        if "leadership_traits" in self.personal_traits:
            print(f"{self.name} exhibits leadership traits. Provides calm guidance to facilitate orderly evacuation.")

    def simulate_alarm_testing(self):
        if random.random() < 0.7:  # 70% chance of participating in an alarm system test
            print(f"{self.name} is participating in an alarm system test. Evaluate effectiveness.")
        else:
            print(f"{self.name} may not be participating in the alarm system test.")

    def practice_escape_routes(self):
        if random.random() < 0.6:  # 60% chance of practicing escape routes
            print(f"{self.name} is practicing escape routes. Enhance knowledge for efficient movement.")
        else:
            print(f"{self.name} may not be practicing escape routes.")

    def experience_simulated_panic(self):
        if random.random() < 0.5:  # 50% chance of simulating panic and disorientation
            print(f"{self.name} is simulating panic and disorientation. Evaluate response in chaotic scenarios.")
        else:
            print(f"{self.name} may not be simulating panic and disorientation.")

    def lead_evacuation_group(self):
        if random.random() < 0.4:  # 40% chance of leading an evacuation group
            print(f"{self.name} is leading an evacuation group. Observe leadership and guidance skills.")
        else:
            print(f"{self.name} may not be leading an evacuation group.")

    def experience_sensory_overload(self, flashing_lights):
        if flashing_lights:
            print(f"{self.name} is disoriented and confused by flashing lights, affecting navigation.")

    def experience_loss_of_balance(self, smoke_inhalation):
        if smoke_inhalation:
            print(f"{self.name} experiences dizziness and impaired coordination, making navigation challenging.")

    def focus_on_immediate_threats(self, fear):
        if fear:
            print(f"{self.name} has tunnel vision, focusing on immediate threats and potentially missing alternative escape routes.")

    def experience_fatigue(self, sudden_awakening):
        if sudden_awakening:
            print(f"{self.name} is groggy and disoriented due to sudden awakening, impacting reaction time.")

    def face_improper_footwear(self, slippery_shoes):
        if slippery_shoes:
            print(f"{self.name} faces tripping hazards and slowed escape due to slippery shoes.")

    def lack_of_knowledge_about_equipment(self, unfamiliarity):
        if unfamiliarity:
            print(f"{self.name} may not know how to operate emergency equipment, hindering self-help or assistance to others.")

    def succumb_to_peer_pressure(self, peer_pressure):
        if peer_pressure:
            print(f"{self.name} hesitates to deviate from the crowd, even if it's leading in the wrong direction.")

    def share_misinformation(self, misinformation):
        if misinformation:
            print(f"{self.name} may spread rumors or false assumptions, contributing to confusion.")

    def face_leadership_vacuum(self, lack_of_guidance):
        if lack_of_guidance:
            print(f"{self.name} experiences a lack of clear guidance, leading to delays and indecisiveness.")

    def encounter_dead_end(self, dead_end):
        if dead_end:
            print(f"{self.name} encounters a dead-end corridor, potentially limiting escape routes.")

    def face_hidden_fire_hazards(self, flammable_items):
        if flammable_items:
            print(f"{self.name} faces hidden fire hazards in dorm rooms with flammable materials, contributing to the spread of fire.")

    def encounter_locked_doors(self, locked_doors):
        if locked_doors:
            print(f"{self.name} encounters locked doors, potentially trapping them in certain areas.")

    def use_windows_as_escape(self, windows):
        if windows:
            print(f"{self.name} considers using windows as escape routes, especially in certain situations.")
        def move_towards_exit(self, exit_position):
            print(f"{self.name} is currently at position {self.position}.")

        while self.position != exit_position:
            direction = input("Enter the direction (up/down/left/right) to move towards the exit: ").lower()

            if direction == "up":
                self.position = (self.position[0], self.position[1] + 1)
            elif direction == "down":
                self.position = (self.position[0], self.position[1] - 1)
            elif direction == "left":
                self.position = (self.position[0] - 1, self.position[1])
            elif direction == "right":
                self.position = (self.position[0] + 1, self.position[1])
            else:
                print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")

            print(f"{self.name} moved to position {self.position}.")

        print(f"{self.name} has reached the exit at position {exit_position}.")
        print("Simulation complete.")

    def move_towards_exit_with_fire(self, exit_position, blocked_positions, fire_likelihood):
        print(f"{self.name} is currently at position {self.position}.")
        print(f"Blocked exits: {blocked_positions}")

        optimized_path = self.calculate_optimized_path(exit_position, blocked_positions, fire_likelihood)

        if not optimized_path:
            print("No optimized path found. Evacuation may be unsafe.")
            return

        for new_position in optimized_path:
            self.position = new_position
            print(f"{self.name} moved to position {self.position}.")

            if self.position == exit_position:
                print(f"{self.name} has reached the exit at position {exit_position}.")
                print("Evacuation successful.")
                return

    def calculate_optimized_path(self, exit_position, blocked_positions, fire_likelihood):
        pq = [(0, self.position, [])]
        visited = set()

        while pq:
            cost, current, path = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)

            if current == exit_position:
                return path + [current]

            for neighbor, weight in self.get_neighbors(current, blocked_positions, fire_likelihood):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [current]))

        return None

    def get_neighbors(self, position, blocked_positions, fire_likelihood):
        x, y = position
        neighbors = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)

                if 0 <= nx < 500 and 0 <= ny < 500 and neighbor not in blocked_positions:
                    weight = fire_likelihood.get(neighbor, 0)
                    neighbors.append((neighbor, weight))

        return neighbors


# Example Usage:
# person1 = Person("John", personal_traits=["panic", "reduced_mobility"])
# person1.enter_building("Main Entrance")
# person1.react_to_emergency("Fire")
# person1.guide_in_smoke()
# person1.provide_assistance()
# person1.follow_instructions("Use Stairs")
# person1.assist_vulnerable_individual("older_adults")
# person1.prioritize_self_preservation()
# person1.share_information("There's a fire on the second floor.")
# person1.leave_building("Emergency Exit")
