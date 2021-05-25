from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timezone
from time import time
from .models import stol,stol_pr
#from django.http import HttpResponse
# Create your views here.
def set_numer(request):
    url='numer/set_numer.html'
    context = {
    }
    if request.method=='POST':
        linia = request.POST.get("linia")
        dziesiatki = request.POST.get("dzies")
        jednostki = request.POST.get("jedn")
        print(dziesiatki,jednostki)
        context['linia']=linia
        context['dziesiatki']=dziesiatki
        context['jednostki']=jednostki
        st = stol.objects.filter(linia=linia).first()
        print(st)
        st.jednostki=jednostki
        st.dziesiatki=dziesiatki
        st.czas_start=datetime.now()
        st.dataczas_start=datetime.now(timezone.utc)
        #st_pr=stol_pr.objects.filter(linia=linia).first()
        #if st_pr.dziesiatki == dziesiatki and st_pr.jednostki == jednostki:
        #    st.zmiana=False
        #else:
        #    st.zmiana=True
        st.save()
    else:
        None
    return render(request,url,context)

#def show_numer_1(request):
#    url='numer/show_numer_1.html'
#    context = {
#    }
#    st = stol.objects.filter(linia=1).first()
#
#    st_pr=stol_pr.objects.filter(linia="1").first()
#    
#    if st_pr.jednostki==st.jednostki and  st_pr.dziesiatki==st.dziesiatki:
#        context['zmiana']=0
#    else:
#        print("zmiana")
#        context['zmiana']=1
#        
#
#    context['wygas'] = 0
#    context['dziesiatki'] = st.dziesiatki
#    context['jednostki'] = st.jednostki
#    st_pr.dziesiatki=st.dziesiatki
#    st_pr.jednostki=st.jednostki
#    st_pr.linia=st.linia
#    st_pr.save()
#    return render(request,url,context)

def show_numer_1(request):

    url='numer/show_numer_1.html'
    context = {
    }
    st = stol.objects.filter(linia=1).first()

    st_pr=stol_pr.objects.filter(linia="1").first()
    
    if st_pr.jednostki==st.jednostki and  st_pr.dziesiatki==st.dziesiatki:
        context['zmiana']=0
        #czas_delta = datetime.now()
        #print(datetime.now(timezone.utc) - st.dataczas_start)
        delta = datetime.now(timezone.utc) - st.dataczas_start
        mins=delta.total_seconds()/60
        if mins>3:
            context['wygas']=0
        else:
            context['wygas']=1
        #print("sss",czas_delta)
        

    else:
        context['zmiana']=1
        czas_start = datetime.now() #.timestamp()


    context['dziesiatki'] = st.dziesiatki
    context['jednostki'] = st.jednostki
    st_pr.dziesiatki=st.dziesiatki
    st_pr.jednostki=st.jednostki
    st_pr.linia=st.linia
    st_pr.save()

    return render(request,url,context)
def show_numer_2(request):

    url='numer/show_numer_2.html'
    context = {
    }
    st = stol.objects.filter(linia=2).first()

    st_pr=stol_pr.objects.filter(linia="2").first()
    
    if st_pr.jednostki==st.jednostki and  st_pr.dziesiatki==st.dziesiatki:
        context['zmiana']=0
        #czas_delta = datetime.now()
        #print(datetime.now(timezone.utc) - st.dataczas_start)
        delta = datetime.now(timezone.utc) - st.dataczas_start
        mins=delta.total_seconds()/60
        if mins>3:
            context['wygas']=0
        else:
            context['wygas']=1
        #print("sss",czas_delta)
        

    else:
        context['zmiana']=1
        czas_start = datetime.now() #.timestamp()


    context['dziesiatki'] = st.dziesiatki
    context['jednostki'] = st.jednostki
    st_pr.dziesiatki=st.dziesiatki
    st_pr.jednostki=st.jednostki
    st_pr.linia=st.linia
    st_pr.save()

    return render(request,url,context)

def show_numer_3(request):

    url='numer/show_numer_3.html'
    context = {
    }
    st = stol.objects.filter(linia=3).first()

    st_pr=stol_pr.objects.filter(linia="3").first()
    
    if st_pr.jednostki==st.jednostki and  st_pr.dziesiatki==st.dziesiatki:
        context['zmiana']=0
        #czas_delta = datetime.now()
        #print(datetime.now(timezone.utc) - st.dataczas_start)
        delta = datetime.now(timezone.utc) - st.dataczas_start
        mins=delta.total_seconds()/60
        if mins>3:
            context['wygas']=0
        else:
            context['wygas']=1
        #print("sss",czas_delta)
        

    else:
        context['zmiana']=1
        czas_start = datetime.now() #.timestamp()


    context['dziesiatki'] = st.dziesiatki
    context['jednostki'] = st.jednostki
    st_pr.dziesiatki=st.dziesiatki
    st_pr.jednostki=st.jednostki
    st_pr.linia=st.linia
    st_pr.save()

    return render(request,url,context)
#def show_numer_3(request):
#    url='numer/show_numer_3.html'
#    context = {
#    }
#    st = stol.objects.filter(linia=3).first()
#
#    st_pr=stol_pr.objects.filter(linia="3").first()
#    
#    if st_pr.jednostki==st.jednostki and  st_pr.dziesiatki==st.dziesiatki:
#        context['zmiana']=0
#    else:
#        print("zmiana")
#        context['zmiana']=1
#
#
#    context['dziesiatki'] = st.dziesiatki
#    context['jednostki'] = st.jednostki
#    st_pr.dziesiatki=st.dziesiatki
#    st_pr.jednostki=st.jednostki
#    st_pr.linia=st.linia
#    st_pr.save()

#    return render(request,url,context)
