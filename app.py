from flask import Flask, render_template, request, redirect, url_for
from utils.auth import register_user, check_admin, check_user
from utils.courier_service import (
    add_courier,
    get_all_couriers,
    search_courier, update_courier_status, delete_courier,report_counts)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if check_admin(username, password):
            return redirect(url_for("admin_dashboard"))

        elif check_user(username, password):
            return redirect(url_for("user_dashboard"))

        else:
            return render_template(
                "login.html",
                error="Invalid Username or Password!"
            )

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        username = request.form["username"]
        password = request.form["password"]

        register_user(name, email, phone, username, password)

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/user_dashboard")
def user_dashboard():

    couriers = get_all_couriers()

    total, delivered, transit, cancelled = report_counts()

    return render_template(
        "user_dashboard.html",
        couriers=couriers,
        total=total,
        delivered=delivered,
        transit=transit
    )


@app.route("/admin_dashboard")
def admin_dashboard():

    total, delivered, transit, cancelled = report_counts()

    return render_template(
        "admin_dashboard.html",
        total=total,
        delivered=delivered,
        transit=transit,
        cancelled=cancelled
    )

@app.route("/add_courier", methods=["GET", "POST"])
def add_courier_page():

    if request.method == "POST":

        tracking_id = add_courier(

            request.form["booking_date"],
            request.form["sender_name"],
            request.form["sender_phone"],
            request.form["sender_address"],
            request.form["receiver_name"],
            request.form["receiver_phone"],
            request.form["receiver_address"],
            request.form["weight"],
            request.form["package_type"],
            request.form["delivery_type"],
            request.form["expected_delivery"]

        )

        return render_template(
            "success.html",
            tracking_id=tracking_id
        )

    return render_template("add_courier.html")

@app.route("/view_couriers")
def view_couriers():

    couriers = get_all_couriers()

    return render_template(
        "view_couriers.html",
        couriers=couriers
    )

@app.route("/search_courier", methods=["GET", "POST"])
def search_courier_page():

    courier = None

    if request.method == "POST":

        tracking_id = request.form["tracking_id"]

        courier = search_courier(tracking_id)

    return render_template(
        "search_courier.html",
        courier=courier
    )

@app.route("/update_status", methods=["GET","POST"])
def update_status():

    message = ""

    if request.method == "POST":

        tracking = request.form["tracking_id"]

        status = request.form["status"]

        if update_courier_status(tracking, status):

            message = "Status Updated Successfully!"

        else:

            message = "Tracking ID Not Found!"

    return render_template(
        "update_status.html",
        message=message
    )

@app.route("/delete_courier", methods=["GET","POST"])
def delete_courier_page():

    message = ""

    if request.method == "POST":

        tracking = request.form["tracking_id"]

        if delete_courier(tracking):

            message = "Courier Deleted Successfully!"

        else:

            message = "Tracking ID Not Found!"

    return render_template(
        "delete_courier.html",
        message=message
    )

@app.route("/track", methods=["GET","POST"])
def track():

    courier = None

    if request.method == "POST":

        tracking = request.form["tracking_id"]

        courier = search_courier(tracking)

    return render_template(
        "track.html",
        courier=courier
    )

@app.route("/reports")
def reports():

    total, delivered, transit, cancelled = report_counts()

    return render_template(
        "reports.html",
        total=total,
        delivered=delivered,
        transit=transit,
        cancelled = cancelled
    )

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)