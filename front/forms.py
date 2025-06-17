from django import forms

class PersonalityForm(forms.Form):
    camino= forms.ChoiceField(required= False, choices= [("caminoPeligroso","El camino corto pero peligroso"),("caminoSeguro","El camino largo pero seguro")])
    hobby= forms.ChoiceField(required= False, choices= [("dormir","Voy a dormir una linda siesta por un rato"),("caminar","Voy a caminar por el barrio hasta que tenga que hacer cosas"),("jugar", "Voy a viciar a los jueguitos"),("socializar", "Voy a hablar con mis amigos")])
    encierro= forms.ChoiceField(required= False, choices= [("gritar","Grito con todas mis fuerzas"),("patear","Pateo la puerta"),("llorar", "Empiezo a llorar")])
  
 