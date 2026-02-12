from flask import Flask, render_template, request
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.scheme_rec import recommend_schemes

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    user = {
        "age": int(request.form["age"]),
        "user_gender": request.form["gender"],
        "income": int(request.form["income"]),
        "state": request.form["state"],
        "category": request.form["category"]
    }

    rec = recommend_schemes(user)

    return render_template(
        "result.html",
        sch=rec.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)
