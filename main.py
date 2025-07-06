from warehouse import warehouse_grid, box_sets
from loader_unit import LoaderUnit
from delivery_unit import DeliveryUnit

def run_simulation():
    loader = LoaderUnit(box_sets)
    delivery_robot = DeliveryUnit()

    while loader.has_more_boxes():
        next_box = loader.get_next_box()

        if next_box:
            box_x, box_y = next_box

            # Move delivery robot to loader
            delivery_robot.move_to(box_x, box_y)

            # Load the box (simulated)
            delivery_robot.load_box()

            # Move back to starting point
            delivery_robot.move_to(*delivery_robot.start_position)

            # Unload the box (simulated)
            delivery_robot.unload_box()
        else:
            loader.move_to_next_set()

if __name__ == "__main__":
    run_simulation()