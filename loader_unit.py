class LoaderUnit:
    def __init__(self, box_sets):
        self.box_sets = box_sets
        self.current_set_index = 0
        self.current_box_index = 0

    def has_more_boxes(self):
        return self.current_set_index < len(self.box_sets)

    def get_next_box(self):
        if self.current_set_index >= len(self.box_sets):
            return None
        current_set = self.box_sets[self.current_set_index]
        if self.current_box_index < len(current_set):
            box = current_set[self.current_box_index]
            self.current_box_index += 1
            return box
        return None

    def move_to_next_set(self):
        self.current_set_index += 1
        self.current_box_index = 0