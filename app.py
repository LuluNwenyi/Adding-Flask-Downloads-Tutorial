
###### TO IMPORT THE DEPENDENCIES #####

from flask import Flask, render_template, url_for, send_file
from werkzeug.exceptions import abort

app = Flask(__name__)

###### CONSTANTS #########
path = "trialdoc.pdf"

###### HOME PAGE ########
@app.route('/')
def index():
     
    return render_template('index.html')

###### DOWNLOAD ROUTE #######
@app.route('/download', methods=['GET', 'POST'])
def return_file():
    try:
        return send_file(path, as_attachment=True)

    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
     app.run(debug=True) # set debug to false before deploying.
