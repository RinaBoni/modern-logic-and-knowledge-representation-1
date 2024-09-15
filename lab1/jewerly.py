class JewelryMaker:
    def __init__(self):
        # Время и проволока для каждого изделия
        self.items = {
            "кольцо": {"time": 15, "thick_wire": 10, "thin_wire": 50},
            "подвеска": {"time": 30, "thick_wire": 40, "thin_wire": 20},
            "браслет": {"time": 420, "thick_wire": 80, "thin_wire": 300}
        }

    def can_make_items(self, available_time, available_thick_wire, available_thin_wire):
        possible_items = []
        for item, requirements in self.items.items():
            if available_time >= requirements["time"] and available_thick_wire >= requirements["thick_wire"] and available_thin_wire >= requirements["thin_wire"]:
                possible_items.append(item)
        return possible_items
    
    def get_item_requirements(self, item_name):
        return self.items.get(item_name, None)
