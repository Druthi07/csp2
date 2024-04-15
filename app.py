from flask import Flask, request, send_file
from nbclient import NotebookClient
from nbformat import read

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    inputprompt = request.form['query']
    
    # Load the notebook
    with open('TextToImageGenerator.ipynb', 'r') as f:
        notebook_content = read(f, as_version=4)

    # Create a notebook client
    nb_client = NotebookClient(notebook_content)

    # Execute the notebook with input
    nb_client.execute(inputprompt)

    # Assuming the output image is saved as output.png
    return send_file('output.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
