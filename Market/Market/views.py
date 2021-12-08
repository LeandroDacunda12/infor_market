from django.shortcuts import render 


def inicio(request):
	usuario = {
		"nombre": "Leandro",
		"apellido": "Dacunda"
	}
	productos = [
		{"nombre" : "computadora","precio": 12},
		{"nombre": "teclado", "precio": 120},

	]

	contex ={
		"usuario": usuario,
		"productos": productos
	}

	return render(request, "inicio.html")
