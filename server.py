from flask import Flask, render_template,request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as file2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(f"{email}, {subject}, {message}")
        csv_writer = csv.writer(file2, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Data could not be saved. :('
    else:
        return 'something went wrong. Try again!'




#calling pages dynamically, instead of repeating code

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
