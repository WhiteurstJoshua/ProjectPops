from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def agreement_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # You can log, store, or process this data
        print(data)
        return "Agreement submitted successfully!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
