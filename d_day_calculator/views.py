from django.shortcuts import render, redirect
from django.template import Context, Template
from .models import EventModel
from .forms import PostEventForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url = 'account:signin')
def view_events(request):
    if request.method == "POST":
        form = PostEventForm(request.POST)
        if form.is_valid():    
            form.save() #일단 세이브
            return redirect('/event')
    else:
        form = PostEventForm()
        not_lastday = EventModel.objects.exclude(is_main = False) #종강일 제외
        lastday = EventModel.objects.get(is_main = True) #종강일만
        lastday_persentage = (lastday.event_date - datetime.date.today()) / (lastday.event_date - lastday.start_date)
        # 여기 list index 오류 나가지고 일단 주석처리 해둠
    #     ctxt = EventModel.objects.exclude(event_name = '종강')[0]
    #     print(type(ctxt.event_date))
        # return render(request,'d_day_calculator/view_events.html', 
        #     {'lastday' : ctxt.event_date, 'form' : form},)
        return render(request, 'd_day_calculator/calc.html', 
            {'lastday' : lastday, 'not_lastday' : not_lastday })

    