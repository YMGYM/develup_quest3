from django.shortcuts import render, redirect
from .forms import PostEventForm

# Create your views here.
def post_event(request):
    if request.method == "POST":
        form = PostEventForm(request.POST) 
        if form.is_valid():
            lotto = form.save(commit = False) 
            lotto.generate()
            return redirect('index') 
    else:
        form = PostEventForm()
        return render(request, 'post_event.html', {'form' : form}) 
