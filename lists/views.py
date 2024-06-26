from lists.models import Item
from django.shortcuts import redirect, render

# Aufgabe: Verarbeitung von Benutzereingaben und Rückgabe einer geeigneten Antwort
# Create your views here.

def home_page(request):
    if request.method == "POST":
        Item.objects.create(text = request.POST["item_text"])
        return redirect("/")
    
    items = Item.objects.all()
    return render(
        request,
        "home.html",
        {"items": items}
        )

