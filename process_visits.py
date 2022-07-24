import time


def check_inside_circle_pythogoras(center_x, center_y, radius, x, y):
    """Check whether a given point lies inside the circle
    with Pythogoras theorem"""

    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2

    return square_dist < radius**2


def check_inside_circle_divisive(center_x, center_y, radius, x, y):
    """Check whether a given point lies inside the circle with the
    divisive approach described in readme answer 1"""

    dx = abs(x - center_x)

    if dx > radius:
        return False

    dy = abs(y - center_y)

    if dy > radius:
        return False

    if dx + dy < radius:
        return True

    return dx * dx + dy * dy < radius**2


def process_visits_pythogoras(raw_data, hotspot_data, stream_generator):
    """Process visits for each data_point using the pythogrean method, for each hotspot, needs a
    stream generator as well as raw and hotspot dataframes as input"""

    all_visits = {}

    total_time = 0

    # iterate over the raw input data with generator

    for input_x, input_y, timestamp in stream_generator:

        start_time = time.time()

        for _, hotspot in hotspot_data.iterrows():  # iterate over all the hotspots

            if hotspot["id"] not in all_visits:
                all_visits[hotspot["id"]] = []

            if check_inside_circle_pythogoras(
                hotspot["x"], hotspot["y"], 5, input_x, input_y
            ):  # check if a hotspot has been visited

                all_visits[hotspot["id"]].append(
                    timestamp
                )  # Mark the hotspot as visited

        end_time = time.time()

        total_time += (
            end_time - start_time
        )  # calculate time taken to execute for one datapoint

    return all_visits, total_time


def process_visits_divisive(raw_data, hotspot_data, stream_generator):
    """Process visits for each data_point using the divisive method, for each hotspot, needs a
    stream generator as well as raw and hotspot dataframes as input"""

    all_visits = {}

    total_time = 0

    # iterate over the raw input data with generator

    for input_x, input_y, timestamp in stream_generator:

        start_time = time.time()

        for _, hotspot in hotspot_data.iterrows():  # iterate over all the hotspots

            if hotspot["id"] not in all_visits:
                all_visits[hotspot["id"]] = []

            if check_inside_circle_divisive(
                hotspot["x"], hotspot["y"], 5, input_x, input_y
            ):  # check if a hotspot has been visited

                all_visits[hotspot["id"]].append(
                    timestamp
                )  # Mark the hotspot as visited

        end_time = time.time()

        total_time += (
            end_time - start_time
        )  # calculate time taken to execute for one datapoint

    return all_visits, total_time
