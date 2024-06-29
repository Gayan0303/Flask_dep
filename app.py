from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for other pages or additional functionality
# Example: adding '/about' page
@app.route('/about')
def about():
    return render_template('about.html')

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
