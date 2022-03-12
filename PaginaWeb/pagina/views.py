from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import hashlib
# Create your views here.
class Inicio(View):
    def get(self,request):
        codificar = Codificar()
        str_codede = codificar.codificador('contrasenia1234');
        print(str_codede.hexdigest())
        return render(request,'pagina/index.html')

class Codificar:
    def codificador(self, cadena):
        resultado = hashlib.sha256(cadena.encode())
        return resultado