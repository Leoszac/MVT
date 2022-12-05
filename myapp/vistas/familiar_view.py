from django.shortcuts import render
from myapp.modelos import Familiar
import datetime

class Familiar_view:

    def autogenerar_listar_familiares(request):
        fm1 = Familiar("Juan", 30, datetime.date(1992, 12, 3))
        fm2 = Familiar("Nicolas", 36, datetime.date(1986, 5, 12))
        fm3 = Familiar("Pedro", 20, datetime.date(2002, 5, 10))

        # fm1 = Familiar.create(  "Leandro", 36, datetime.date(1988, 5, 12)  )

        fm1.save()
        fm2.save()
        fm3.save()



        return render(request,'autogenerar_listar_familiares.html', {"familiares": [fm1, fm2, fm3]} )


