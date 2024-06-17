import sys
import io
import subprocess  # New import for subprocess
import webbrowser  # New import for webbrowser
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define a form for code input
class CodeForm(FlaskForm):
    code = TextAreaField('Enter your Python code:', validators=[DataRequired()])
    submit = SubmitField('Run')

# Function to execute Python code and capture output
def execute_python(code):
    try:
        # Capture stdout to retrieve output of executed code
        stdout = sys.stdout
        sys.stdout = io.StringIO()

        exec(code)
        output = sys.stdout.getvalue()

    except Exception as e:
        output = f"Error: {str(e)}"
    
    finally:
        # Restore stdout
        sys.stdout = stdout

    return output

# Function to install required packages
def install_required_packages():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask', 'flask-wtf', 'wtforms'])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    output = None

    if form.validate_on_submit():
        code = form.code.data.strip()
        output = execute_python(code)

    return render_template('index.html', form=form, output=output)

if __name__ == '__main__':
    # Install required packages
    install_required_packages()

    # Open web browser automatically after starting the app
    webbrowser.open('http://localhost:22341/')

    # Run the Flask application
    app.run(debug=True, port=22341, host='0.0.0.0')
