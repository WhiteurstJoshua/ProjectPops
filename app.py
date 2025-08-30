from flask import Flask, render_template, request, send_file
import contract_generator
import tempfile
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.to_dict()

        temp_path = tempfile.mktemp(suffix=".docx")
        contract_generator.build_agreement(data, output_path=temp_path)

        return send_file(temp_path, as_attachment=True, download_name="Generated_Agreement.docx")

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
