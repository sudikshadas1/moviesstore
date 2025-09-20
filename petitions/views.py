from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Petition, PetitionVote

def index(request):
    petitions = Petition.objects.all().order_by('-created_at')
    return render(request, "petitions/index.html", {"petitions": petitions})

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Petition.objects.create(title=title, description=description, created_by=request.user)
        return redirect("petitions.index")
    return render(request, "petitions/create.html")

@login_required
def vote(request, id):
    petition = get_object_or_404(Petition, id=id)
    # Only allow "YES" votes
    PetitionVote.objects.get_or_create(petition=petition, user=request.user, defaults={"choice": "YES"})
    return redirect("petitions.index")
