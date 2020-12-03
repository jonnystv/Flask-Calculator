from app import app

from modules import calculator

@app.route("/add/<num_1>/<num_2>")
def add_2_numbers(num_1, num_2):
    return f"The answer to {num_1} plus {num_2} is {int(num_1) + int(num_2)}"


@app.route("/subtract/<num_1>/<num_2>")
def subtract_2_numbers(num_1, num_2):
    return f"The answer to {num_1} minus {num_2} is {int(num_1) - int(num_2)}"


@app.route("/multiply/<num_1>/<num_2>")
def multiply_2_numbers(num_1, num_2):
    return f"The answer to {num_1} mutiplied by {num_2} is {int(num_1) * int(num_2)}"


@app.route("/divide/<num_1>/<num_2>")
def divide_2_numbers(num_1, num_2):
    return f"The answer to {num_1} divided by {num_2} is {int(num_1) / int(num_2)}"