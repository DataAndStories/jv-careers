# FLASK WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# from flask module, import class Flask
# jsonify .. to retun json of the job list (not as html)
from flask import Flask, render_template, jsonify

# create app, an object of class Flask
app = Flask(__name__)

# jobs
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$150,000'
    }
]

# index page as home.html
# pass job as a list to html - create an html endpoint
# define the company name as a variable for using in html


@app.route("/")
def home():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name="Jovian")

# instead of retning as html, let's return as JSON - create an JSON endpoint


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


# debug = true .. refresh the page to see the changes
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
