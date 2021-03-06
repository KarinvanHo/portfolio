from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        database.write(f'\n{data["email"]},{data["subject"]},{data["message"]}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])


@app.route('/index.html')
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again.'
