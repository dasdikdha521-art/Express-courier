import csv
from utils.helpers import generate_tracking_id

COURIER_FILE = "data/couriers.csv"


def add_courier(
    booking_date,
    sender_name,
    sender_phone,
    sender_address,
    receiver_name,
    receiver_phone,
    receiver_address,
    weight,
    package_type,
    delivery_type,
    expected_delivery
):

    if delivery_type == "Normal":
        charges = 80
    else:
        charges = 150

    tracking_id = generate_tracking_id()

    status = "Booked"

    with open(COURIER_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            tracking_id,
            booking_date,
            sender_name,
            sender_phone,
            sender_address,
            receiver_name,
            receiver_phone,
            receiver_address,
            weight,
            package_type,
            delivery_type,
            charges,
            expected_delivery,
            status
        ])

    return tracking_id

def get_all_couriers():

    couriers = []

    with open("data/couriers.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)   # Skip header

        for row in reader:
            couriers.append(row)

    return couriers

def search_courier(tracking_id):

    with open("data/couriers.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[0] == tracking_id:

                return row

    return None

def update_courier_status(tracking_id, new_status):

    import csv

    updated = False

    rows = []

    with open("data/couriers.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and row[0] == tracking_id:

                row[13] = new_status

                updated = True

            rows.append(row)

    with open("data/couriers.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

    return updated

def delete_courier(tracking_id):

    import csv

    deleted = False

    rows = []

    with open("data/couriers.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and row[0] == tracking_id:

                deleted = True
                continue

            rows.append(row)

    with open("data/couriers.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerows(rows)

    return deleted

def report_counts():

    total = 0
    delivered = 0
    transit = 0
    cancelled = 0

    with open("data/couriers.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            total += 1

            status = row[13].strip()

            if status == "Delivered":
                delivered += 1

            elif status == "In Transit":
                transit += 1

            elif status == "Cancelled":
                cancelled += 1

    return total, delivered, transit, cancelled