from pytube import Search
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



ytsearch('imagin dragon')
