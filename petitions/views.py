from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Petition, Vote

def index(request):
    petitions = Petition.objects.all().order_by('-created_at')
    template_data = {'title': 'Petitions'}
    return render(request, 'petitions/index.html', {'petitions': petitions, 'template_data': template_data})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Petition.objects.create(title=title, description=description, user=request.user)
        return redirect('petitions.index')
    return render(request, 'petitions/create.html')

@login_required
def vote(request, id):
    petition = get_object_or_404(Petition, id=id)
    # Create or update a vote (only Yes allowed for now)
    vote, created = Vote.objects.update_or_create(
        petition=petition, user=request.user, defaults={'choice': 'YES'}
    )
    
    # Update the yes_votes count
    petition.yes_votes = petition.votes.filter(choice='YES').count()
    petition.save()
    
    return redirect('petitions.index')


