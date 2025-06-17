from django.shortcuts import render
from django.views import View
from .forms import PersonalityForm
# Create your views here.
class PersonalityIndex(View):
    template_name = 'pages/primera.html'
    def calcularPuntaje(self, camino, hobby, encierro):
        amigable = 0
        miedoso = 0
        aventurero = 0
        vago = 0
        if camino == "caminoPeligroso":
            aventurero += 1
            amigable += 1
        elif camino == "caminoSeguro":
            miedoso += 2
            vago += 1
        
        if hobby == "dormir":
            vago += 2
        elif hobby == "caminar":
            aventurero += 1
        elif hobby == "jugar":
            miedoso +=  1
        elif hobby == "socializar":
            amigable +=  2

        if encierro == "gritar":
            miedoso +=  1
        elif encierro == "patear":
            aventurero +=  1
        elif encierro == "llorar":
            amigable +=  1
      
        if miedoso > amigable and miedoso > aventurero and miedoso > vago:
            return("¡Sos Cubone! Un pokemon miedoso")
        elif amigable > miedoso and amigable > aventurero and amigable > vago:
            return("¡Sos Pikachu! Un pokemon amigable")
        elif aventurero > amigable and aventurero > miedoso and aventurero > vago:
            return("¡Sos Charmander! Un pokemon aventurero")
        elif vago > amigable and vago > miedoso and vago > aventurero:
            return ("¡Sos Munchlax! Un pokemon vago")
        else :
            return("¡Sos Eevee! Un pokemon con una personalidad única.")
        
    def get(self, request):
        context = {
            "form" : PersonalityForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = PersonalityForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            camino = form.cleaned_data["camino"]
            hobby = form.cleaned_data["hobby"]
            encierro = form.cleaned_data["encierro"]
            resultado = self.calcularPuntaje(camino, hobby, encierro)
            context['result'] = resultado
        return render(request, self.template_name, context)