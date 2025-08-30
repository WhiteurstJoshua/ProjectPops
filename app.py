from flask import Flask, render_template, request, send_file
import contract_generator
import tempfile
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = {
            'client_name': request.form['client_name'],
            'role': request.form['role'],
            'scope': request.form['scope'],
            'payment_type': request.form['payment_type'],
            'hourly_rate': request.form.get('hourly_rate', ''),
            'total_payment': request.form['total_payment'],
            'insurance': request.form['insurance']
        }

        # Create a temporary file for the generated contract
        temp_path = tempfile.mktemp(suffix=".docx")
        contract_generator.build_agreement(data, output_path=temp_path)

        return send_file(temp_path, as_attachment=True, download_name="Generated_Agreement.docx")

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
