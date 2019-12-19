from django.shortcuts import render
import requests
from . import parse


def button(request):
	return render(request, 'home.html')

def calc(request):
	date = request.POST.get('param1')
	city = request.POST.get('param2')
	out = parse.AVG(date, city)
	if len(out) == 3:
		temp, pres, speed = str(out[0]) + '°C', str(out[1]) + 'мм.рт.ст.', str(out[2]) + 'м/с'
		message = ''
		return render(request, 'home.html', {'mess': message, 'temp': temp, 'pres': pres, 'speed': speed})
	else:
		temp, pres, speed = ['-', '-', '-']
		message = out
		return render(request, 'home.html', {'mess': message, 'temp': temp, 'pres': pres, 'speed': speed})