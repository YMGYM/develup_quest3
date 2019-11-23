from django.shortcuts import render, redirect
from .forms import PostEventForm

# Create your views here.
def post_event(request):
    if request.method == "POST":
        form = PostEventForm(request.POST) 
        if form.is_valid():
            evt = form.save(commit = False) 
            evt.generate()
            return redirect('index') 
    else:
        form = PostEventForm()
        return render(request, 'post_event.html', {'form' : form})

def view_events(request):
    return render(request,'view_events.html')
