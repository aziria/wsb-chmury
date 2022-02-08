from flask import Flask, render_template, request
from AzureDB import AzureDB

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    with AzureDB() as a:
        if request.method == 'POST':
            product = request.form.get('product')
            details = request.form.get('details')
            a.azureAddData(product, details)

        data = a.azureGetData()
    return render_template('index.html', data2=data)


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
