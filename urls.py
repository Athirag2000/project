from django.urls import path
from . import views

urlpatterns = [
    path('stressapp/', views.stressapp, name='stressapp'),
]

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_candidate, name='register'),
    # Add other URL patterns for other views if needed
]
# urls.py
from django.urls import path
from . import views

# stressapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a URL pattern for the root URL ('/')
    path('register/', views.register, name='register'),
    # Add other URL patterns as needed...
]

# stressapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('predict-stress/', views.predict_stress_level, name='predict_stress'),
    # Add other URL patterns as needed...
]


