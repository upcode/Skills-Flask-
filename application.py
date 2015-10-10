from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    print "index page working"

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_form():
    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application_response():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    jobs = request.form.get("jobs")
    return render_template("application-response.html", firstname=firstname, lastname=lastname, salary=salary, jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)
