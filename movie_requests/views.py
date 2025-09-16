from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MovieRequest
from .forms import MovieRequestForm

@login_required
def requests_page(request):
    if request.method == "POST":
        form = MovieRequestForm(request.POST)
        if form.is_valid():
            mr = form.save(commit=False)
            mr.user = request.user
            mr.save()
            return redirect('movie_requests:index')
    else:
        form = MovieRequestForm()

    my_requests = MovieRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'movie_requests/index.html', {
        'form': form,
        'requests': my_requests,
    })

@login_required
def delete_request(request, id):
    mr = get_object_or_404(MovieRequest, id=id, user=request.user)
    if request.method == 'POST':
        mr.delete()
        return redirect('movie_requests:index')
    # Simple confirm page could be added; for now just delete on POST
    return redirect('movie_requests:index')
