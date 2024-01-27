class Building:
    def __init__(self, name):
        self.name = name
        self.fire_suppression_system = self.get_user_input("Does the building have a fire suppression system? (yes/no)")
        self.smoke_detectors_and_alarms = self.get_user_input("Are there smoke detectors and alarms installed in all areas? (yes/no)")
        self.emergency_lighting = self.get_user_input("Is there emergency lighting installed in all areas? (yes/no)")
        self.fire_doors = self.get_user_input("Are all fire doors in good condition and not blocked or propped open? (yes/no)")
        self.fire_resistant_materials = self.get_user_input("Is the building constructed with fire-resistant materials? (yes/no)")
        self.evacuation_plan = self.get_user_input("Is there an evacuation plan with multiple exit routes and safe areas? (yes/no)")
        self.training = self.get_user_input("Is training provided to all residents on fire safety and evacuation procedures? (yes/no)")
        self.accessibility = self.get_user_input("Is the building accessible to individuals with disabilities? (yes/no)")
        self.communication_plan = self.get_user_input("Is there a communication plan to keep residents informed about fire safety and evacuation procedures? (yes/no)")
        self.maintenance = self.get_user_input("Is the building well-maintained, and is all fire safety equipment in good working order? (yes/no)")
        self.fire_drills = self.get_user_input("Are regular fire drills conducted to ensure residents are familiar with evacuation procedures? (yes/no)")
        self.emergency_contact_information = self.get_user_input("Do all residents have access to emergency contact information, including the local fire department's phone number? (yes/no)")
        self.safe_areas = self.get_user_input("Are safe areas within the building identified where residents can take refuge in case of a fire? (yes/no)")
        self.fire_resistant_furniture = self.get_user_input("Is all furniture in the building fire-resistant? (yes/no)")
        self.fire_resistant_bedding = self.get_user_input("Is all bedding in the building fire-resistant? (yes/no)")
        self.fire_resistant_curtains = self.get_user_input("Are all curtains in the building fire-resistant? (yes/no)")
        self.fire_resistant_carpeting = self.get_user_input("Is all carpeting in the building fire-resistant? (yes/no)")
        self.fire_resistant_doors = self.get_user_input("Are all doors in the building fire-resistant? (yes/no)")
        self.fire_resistant_windows = self.get_user_input("Are all windows in the building fire-resistant? (yes/no)")
        self.fire_resistant_paint = self.get_user_input("Is all paint used in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation = self.get_user_input("Is all insulation used in the building fire-resistant? (yes/no)")
        self.fire_resistant_roofing = self.get_user_input("Is the building’s roof constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_siding = self.get_user_input("Is the building’s siding constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_landscaping = self.get_user_input("Is the landscaping around the building fire-resistant? (yes/no)")
        self.fire_resistant_storage = self.get_user_input("Are all storage areas in the building constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_appliances = self.get_user_input("Are all appliances in the building fire-resistant? (yes/no)")
        self.fire_resistant_wiring = self.get_user_input("Is all wiring in the building fire-resistant? (yes/no)")
        self.fire_resistant_plumbing = self.get_user_input("Is all plumbing in the building fire-resistant? (yes/no)")
        self.fire_resistant_hvac_systems = self.get_user_input("Are all HVAC systems in the building fire-resistant? (yes/no)")
        self.fire_resistant_elevators = self.get_user_input("Are all elevators in the building fire-resistant? (yes/no)")
        self.fire_resistant_stairwells = self.get_user_input("Are all stairwells in the building constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_hallways = self.get_user_input("Are all hallways in the building constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_ceilings = self.get_user_input("Are all ceilings in the building constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_walls = self.get_user_input("Are all walls in the building constructed with fire-resistant materials? (yes/no)")
        self.fire_resistant_insulation_around_pipes = self.get_user_input("Is all insulation around pipes in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_ducts = self.get_user_input("Is all insulation around ducts in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_wiring = self.get_user_input("Is all insulation around electrical wiring in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_hvac_systems = self.get_user_input("Is all insulation around HVAC systems in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_plumbing = self.get_user_input("Is all insulation around plumbing in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_elevators = self.get_user_input("Is all insulation around elevators in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_stairwells = self.get_user_input("Is all insulation around stairwells in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_hallways = self.get_user_input("Is all insulation around hallways in the building fire-resistant? (yes/no)")
        self.fire_resistant_insulation_around_ceilings = self.get_user_input("Is all insulation around ceilings in the building fire-resistant? (yes/no)")

    def get_user_input(self, prompt):
        user_input = input(prompt).lower()
        return user_input == 'yes'
    def ensure_fire_suppression_system(self):
        if self.fire_suppression_system:
            print(f"The building has an adequate fire suppression system, such as sprinklers or fire extinguishers.")

    def ensure_smoke_detectors_and_alarms(self):
        if self.smoke_detectors_and_alarms:
            print(f"The building has smoke detectors and alarms installed in all areas, including sleeping rooms and common areas.")

    def ensure_emergency_lighting(self):
        if self.emergency_lighting:
            print(f"The building has emergency lighting installed in all areas, including stairwells and hallways.")

    def ensure_fire_doors(self):
        if self.fire_doors:
            print(f"All fire doors in the building are in good condition and are not blocked or propped open.")

    def ensure_fire_resistant_materials(self):
        if self.fire_resistant_materials:
            print(f"The building is constructed with fire-resistant materials, such as fire-resistant drywall and insulation.")

    def develop_evacuation_plan(self):
        if self.evacuation_plan:
            print(f"An evacuation plan is developed, including multiple exit routes and safe areas to gather outside the building.")

    def provide_training(self):
        if self.training:
            print(f"Training is provided to all residents on fire safety and evacuation procedures.")

    def ensure_accessibility(self):
        if self.accessibility:
            print(f"The building is accessible to individuals with disabilities, including those who use wheelchairs or other mobility devices.")

    def establish_communication_plan(self):
        if self.communication_plan:
            print(f"A communication plan is established to keep residents informed about fire safety and evacuation procedures.")

    def ensure_maintenance(self):
        if self.maintenance:
            print(f"The building is well-maintained, and all fire safety equipment is in good working order.")

    def conduct_fire_drills(self):
        if self.fire_drills:
            print(f"Regular fire drills are conducted to ensure that all residents are familiar with evacuation procedures.")

    def ensure_emergency_contact_information(self):
        if self.emergency_contact_information:
            print(f"All residents have access to emergency contact information, including the phone number for the local fire department.")

    def identify_safe_areas(self):
        if self.safe_areas:
            print(f"Safe areas within the building are identified where residents can take refuge in case of a fire.")

    def ensure_fire_resistant_furniture(self):
        if self.fire_resistant_furniture:
            print(f"All furniture in the building is fire-resistant.")

    def ensure_fire_resistant_bedding(self):
        if self.fire_resistant_bedding:
            print(f"All bedding in the building is fire-resistant.")

    def ensure_fire_resistant_curtains(self):
        if self.fire_resistant_curtains:
            print(f"All curtains in the building are fire-resistant.")

    def ensure_fire_resistant_carpeting(self):
        if self.fire_resistant_carpeting:
            print(f"All carpeting in the building is fire-resistant.")

    def ensure_fire_resistant_doors(self):
        if self.fire_resistant_doors:
            print(f"All doors in the building are fire-resistant.")

    def ensure_fire_resistant_windows(self):
        if self.fire_resistant_windows:
            print(f"All windows in the building are fire-resistant.")

    def ensure_fire_resistant_paint(self):
        if self.fire_resistant_paint:
            print(f"All paint used in the building is fire-resistant.")

    def ensure_fire_resistant_insulation(self):
        if self.fire_resistant_insulation:
            print(f"All insulation used in the building is fire-resistant.")

    def ensure_fire_resistant_roofing(self):
        if self.fire_resistant_roofing:
            print(f"The building’s roof is constructed with fire-resistant materials.")

    def ensure_fire_resistant_siding(self):
        if self.fire_resistant_siding:
            print(f"The building’s siding is constructed with fire-resistant materials.")

    def ensure_fire_resistant_landscaping(self):
        if self.fire_resistant_landscaping:
            print(f"The landscaping around the building is fire-resistant.")

    def ensure_fire_resistant_storage(self):
        if self.fire_resistant_storage:
            print(f"All storage areas in the building are constructed with fire-resistant materials.")

    def ensure_fire_resistant_appliances(self):
        if self.fire_resistant_appliances:
            print(f"All appliances in the building are fire-resistant.")

    def ensure_fire_resistant_wiring(self):
        if self.fire_resistant_wiring:
            print(f"All wiring in the building is fire-resistant.")

    def ensure_fire_resistant_plumbing(self):
        if self.fire_resistant_plumbing:
            print(f"All plumbing in the building is fire-resistant.")

    def ensure_fire_resistant_hvac_systems(self):
        if self.fire_resistant_hvac_systems:
            print(f"All HVAC systems in the building are fire-resistant.")

    def ensure_fire_resistant_elevators(self):
        if self.fire_resistant_elevators:
            print(f"All elevators in the building are fire-resistant.")

    def ensure_fire_resistant_stairwells(self):
        if self.fire_resistant_stairwells:
            print(f"All stairwells in the building are constructed with fire-resistant materials.")

    def ensure_fire_resistant_hallways(self):
        if self.fire_resistant_hallways:
            print(f"All hallways in the building are constructed with fire-resistant materials.")

    def ensure_fire_resistant_ceilings(self):
        if self.fire_resistant_ceilings:
            print(f"All ceilings in the building are constructed with fire-resistant materials.")

    def ensure_fire_resistant_walls(self):
        if self.fire_resistant_walls:
            print(f"All walls in the building are constructed with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_pipes(self):
        if self.fire_resistant_insulation_around_pipes:
            print(f"All pipes in the building are insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_ducts(self):
        if self.fire_resistant_insulation_around_ducts:
            print(f"All ducts in the building are insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_wiring(self):
        if self.fire_resistant_insulation_around_wiring:
            print(f"All electrical wiring in the building is insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_hvac_systems(self):
        if self.fire_resistant_insulation_around_hvac_systems:
            print(f"All HVAC systems in the building are insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_plumbing(self):
        if self.fire_resistant_insulation_around_plumbing:
            print(f"All plumbing in the building is insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_elevators(self):
        if self.fire_resistant_insulation_around_elevators:
            print(f"All elevators in the building are insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_stairwells(self):
        if self.fire_resistant_insulation_around_stairwells:
            print(f"All stairwells in the building are insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_hallways(self):
        if self.fire_resistant_insulation_around_hallways:
            print(f"All hallways in the building are insulated with fire-resistant materials.")

    def ensure_fire_resistant_insulation_around_ceilings(self):
        if self.fire_resistant_insulation_around_ceilings:
            print(f"All ceilings in the building are insulated with fire-resistant materials.")
