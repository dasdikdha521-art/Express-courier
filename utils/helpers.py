def generate_tracking_id():

    file = open("data/couriers.csv", "r")

    lines = file.readlines()

    file.close()

    count = len(lines)

    tracking_id = "TRK" + str(1000 + count)

    return tracking_id