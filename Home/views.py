
from django.shortcuts import render
from pytube import YouTube,Search,Playlist
from .models import history


# Create your views here.
def Home(request):
 
    data=playlist(request)
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


def get_link(list,qcode,formate):
    l2=list[formate]
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
        dlink=get_link(l1,140,'adaptiveFormats')
        Vtitle=video.title
        user= request.user.id
        tags = video.keywords
        data = history(title=Vtitle,ytlink=ytlink,dtlink=dlink,tags=tags,user=user)
        data.save()
    except:
        pass
    return render(request,'dl.html',{'dlink':dlink,'title':Vtitle,'elink':url,'data':data_out, 'get_requested':get_requested})



 
def searchRequest(request):
    list=[]
    try:
        keyword=request.GET["searchOverlay"]
        list = ytsearch(keyword)
        data=playlist(request)
    except:
        pass      
    return render(request,'search.html',{'slist':list,'data':data,'search':True})
        
            

def ytsearch(keyword):
    Sobj = Search(keyword)
    list=Sobj.results
    dict =[]
    for i in list:
        d=i.streaming_data
        l2 = d['adaptiveFormats']
        for x in l2:
            if x['itag']==140:
                dict.append([i.title,i.length,i.thumbnail_url,i.views,x['url'],])
    return dict




def managePlaylist(request):
    try:
            link=""
            playlist_download_links=[]
            link=request.GET["playlist_link"]
            p = Playlist(link)
            for i in p.videos:
                l1=i.streaming_data
                dlink=get_link(l1,22,'formats')
                playlist_download_links.append(dlink)
                #dlink=get_link(l1,140)

            
            print(playlist_download_links)
    except:
        print('hi')
    return render(request,'playlist.html',{'pdlink':playlist_download_links})


    