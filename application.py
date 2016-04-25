from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def return_app_form():
    """Show an index page."""

    return render_template("application-form.html")

@app.route("/application")
def process_app_form():
    """Show an index page."""
    first_name = request.args.get('firstname').title()
    last_name = request.args.get('lastname').title()
    req_salary = float(request.args.get('salary'))
    print first_name, last_name, req_salary
    return render_template("application-response.html", firstname=first_name, lastname = last_name, salary = req_salary)


if __name__ == "__main__":
    app.run(debug=True)
