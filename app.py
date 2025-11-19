from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        DNA = request.form["dna"]
        A = T = C = G = 0

        for x in DNA:
            if x.upper() == "A":
                A += 1
            elif x.upper() == "T":
                T += 1
            elif x.upper() == "C":
                C += 1
            elif x.upper() == "G":
                G += 1

        Total = len(DNA)

        resultado = {
            "A": round((A / Total) * 100, 2),
            "T": round((T / Total) * 100, 2),
            "C": round((C / Total) * 100, 2),
            "G": round((G / Total) * 100, 2)
        }

    return render_template("index.html", resultado=resultado)

app.run(debug=True)
