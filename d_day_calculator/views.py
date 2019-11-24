from django.shortcuts import render, redirect
from django.template import Context, Template
from .models import EventModel
from .forms import PostEventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_event(request):
    if request.method == "POST":
        form = PostEventForm(request.POST) 
        if form.is_valid():
            evt = form.save(commit = False) 
            return redirect('event') 
    else:
        form = PostEventForm()
        return render(request, 'd_day_calculator/post_event.html', {'form' : form})

@login_required(login_url = 'acount:signin')
def view_events(request):
    if request.method == "POST":
        form = PostEventForm(request.POST)
        if form.is_valid():    
            form.save() #일단 세이브
            return redirect('/event')
    else:
        form = PostEventForm()
        percentage = '30%'
        ctxt = EventModel.objects.exclude(event_name = '종강')[0]
        print(type(ctxt.event_date))
        return render(request,'d_day_calculator/view_events.html', 
            {'lastday' : ctxt.event_date, 'form' : form},)

    