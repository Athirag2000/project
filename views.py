
from django.http import HttpResponse
from django.template import loader

def stressapp(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm



# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm




# views.py
from django.shortcuts import render, redirect
from .forms import CandidateRegistrationForm



# views.py
from django.shortcuts import render, redirect
from .forms import CandidateRegistrationForm
# views.py
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def register_candidate(request):
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of the view to show a success message
    else:
        form = CandidateRegistrationForm()
    return render(request, 'registrationform.html', {'form': form})

# views.py
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# stressapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Replace 'home.html' with the template for your home page


# stressapp/views.py
from django.shortcuts import render

def register(request):
    # Add your view logic here
    return render(request, 'register.html')  # Replace 'register.html' with the template for the registration page


# stressapp/views.py
import os
import joblib
from django.shortcuts import render
from .forms import StressPredictionForm

# Load the trained ML model
model_path = os.path.join(os.path.dirname(__file__), '..', 'ml_models', 'stress_model.pkl')
loaded_model = joblib.load(model_path)

def predict_stress_level(request):
    if request.method == 'POST':
        form = StressPredictionForm(request.POST)
        if form.is_valid():
            # Get the input parameters from the form
            respiration_rate = form.cleaned_data['respiration_rate']
            body_temperature = form.cleaned_data['body_temperature']
            blood_oxygen_levels = form.cleaned_data['blood_oxygen_levels']
            eye_movement = form.cleaned_data['eye_movement']
            hours_of_sleep = form.cleaned_data['hours_of_sleep']

            # Make the prediction using the loaded model
            input_data = [[respiration_rate, body_temperature, blood_oxygen_levels, eye_movement, hours_of_sleep]]
            stress_level = loaded_model.predict(input_data)[0]

            return render(request, 'result.html', {'stress_level': stress_level})

    else:
        form = StressPredictionForm()

    return render(request, 'predict_stress.html', {'form': form})
