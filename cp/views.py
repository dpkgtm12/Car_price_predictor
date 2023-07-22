from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
import numpy as np
modeL_p= joblib.load('D:\Projects\Car Price Predict\car_price\cp\model.joblib')

# make a prediction




def home(request):
   return render(request, "index.html", {})
def about(request):
   return render(request, "about.html", {})

def calc(request):
   if request.method == 'POST':
        brand=request.POST['brand']
        model=request.POST['model']
        year = request.POST['year']
        kms_driven=request.POST['kms_driven']
        fuel=request.POST['fuel']
        X_new =pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([model,brand,year,kms_driven,fuel]).reshape(1, 5))
        y_pred = modeL_p.predict(X_new)
        return HttpResponse(y_pred)
   else:
      return HttpResponse("Hello")

def form(request):
   years = range(1980, 2024)
   return render(request, "form.html",{'years': years})
def contact(request):
   return render(request, "contact.html",{})
def services(request):
   return render(request, "service.html",{})
def blog(request):
   return render(request, "comment.html",{})

# Create your views here.
