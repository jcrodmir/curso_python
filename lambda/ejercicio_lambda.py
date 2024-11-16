frases=["Los lunes son los mejores días para programar","Python es moderno","Veremos Inteligencia Artificial más adelante", "Lambda simplifica el código"]

frases.sort(key= lambda e: len(e), reverse=True)

#No tiene en cuenta los espacios
#frases.sort(key= lambda e: len(e.split()), reverse=True)

print(frases)
