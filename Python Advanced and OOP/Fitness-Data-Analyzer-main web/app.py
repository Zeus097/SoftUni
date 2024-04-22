from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Calculation functions
def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    body_mass_index = weight / height ** 2
    return body_mass_index

def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    burned_calories_per_minute = 6.67
    estimated_burned_calories = burned_calories_per_minute * duration
    return estimated_burned_calories

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        duration = float(request.form.get('duration'))

        # Perform calculations
        bmi = calculate_bmi(weight, height)
        calories_burned = calculate_calories_burned(duration)

        # Prepare data to pass to the results template
        data = {
            'name': name,
            'bmi': round(bmi, 2),
            'calories_burned': round(calories_burned, 2)
        }
        
        return render_template('results.html', data=data)

    return 'Method Not Allowed', 405


if __name__ == '__main__':
    app.run(debug=True)
