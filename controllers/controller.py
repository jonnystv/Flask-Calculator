from app import app

from modules import calculator

@app.route("/add/<num_1>/<num_2>")
def add_2_numbers(num_1, num_2):
    return f"The answer to {num_1} plus {num_2} is {int(num_1) + int(num_2)}"