from .models import History

def historial(Prod, Usuario, Entry):
    History.objects.create(prod = Prod, user = Usuario, entry = Entry)