
from django.shortcuts import render
from pytube import YouTube
from .models import history


# Create your views here.
def Home(request):
 
    data=playlist(request)
    print(data)
    return render(request,'index.html',{'data':data})






def playlist(request):
    user= request.user.id
    data=history.objects.filter(user=user).values().order_by('hid').reverse()
    return data

def cheak_duplicate(ytlink):
    data =history.objects.filter(ytlink=ytlink).values()
    if len(data) == 0:
        print('False')
    else:
        hid_list=[]
        print('True')
        for i in data:
            hid_list.append((i['hid']))
        print(hid_list) 
        del_duplicate(hid_list)   

def del_duplicate(hid_list):
    for i in hid_list:
        history.objects.filter(hid=i).delete()


def get_link(list,qcode):
    l2=list['formats']
    for i in l2:
        if i['itag']==qcode:
            link = i['url']
            break
    return link

# Create your views here.
def get_audio_data(request):
    data_out=playlist(request)
    try:
        get_requested = False
        if request.method == 'GET':
            get_requested = True

        url="yt.com"
        dlink="yt.com"
        Vtitle="musicverse"
        tags="yt.com"
        ytlink=request.GET['searchOverlay']
        url= ytlink
        cheak_duplicate(url)
        url= url.replace("watch?v=", "embed/")
        video = YouTube(ytlink)
        l1=video.streaming_data
        dlink=get_link(l1,18)
        Vtitle=video.title
        user= request.user.id
        tags = video.keywords
        data = history(title=Vtitle,ytlink=ytlink,dtlink=dlink,tags=tags,user=user)
        data.save()
    except:
        pass
    return render(request,'dl.html',{'dlink':dlink,'title':Vtitle,'elink':url,'data':data_out, 'get_requested':get_requested})



 
        
        
            

