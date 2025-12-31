from flask import Flask, render_template, request
import sympy as sp
import numpy as np

app = Flask(__name__)

x = sp.symbols('x')

@app.route("/", methods=["GET","POST"])
def home():
    result = ""

    if request.method == "POST":
        mode = request.form["mode"]
        expr = request.form["expr"]

        try:
            if mode == "calc":
                result = sp.simplify(expr)

            elif mode == "trig":
                result = sp.N(sp.simplify(expr))

            elif mode == "derivative":
                result = sp.diff(expr, x)

            elif mode == "equation":
                result = sp.solve(expr, x)

            elif mode == "regression":
                data = eval(expr)
                xs, ys = zip(*data)
                a, b = np.polyfit(xs, ys, 1)
                result = f"y = {a:.3f}x + {b:.3f}"

        except:
            result = "Invalid Input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
