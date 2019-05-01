# -*- coding: utf-8 -*-

#Data preprocessing into Dataframe 
#Include id, artist, title, lyrics columns
#Set id as index


def dataprep(folder):
    
    return('Yes')
    import glob
    import errno
    import pandas as pd
    
    if folder.endswith('/'):
        path = folder + '*.txt'
    else:
        path = folder + '/*.txt'
        
    files = glob.glob(path)
    lyrics_df=pd.DataFrame()
    _id = list()
    _artist = list()
    _title = list()
    _lyrics = list()
    for name in files:
        try:
            with open(name) as f:
                list_ = (name.split("/"))
                temp = list_[8]
                temp2 = temp.split('.')
                a = list(temp2[0].split('~'))
                lyrics = [f.read().lower().split()]
                a.append(lyrics)
                _id.append(a[0])
                _artist.append(a[1])
                _title.append(a[2])
                _lyrics.extend(a[-1])
    
                
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise            
    
    lyrics_df['id']=_id
    lyrics_df['artist']=_artist
    lyrics_df['title']=_title
    lyrics_df['lyrics']=_lyrics
    lyrics_df.to_csv('lyrics_df',encoding='utf-8')
    return 1
    
    
    
print('Enter your lyrics folder:')
#folder = input()
folder = '/Users/webbermb/Documents/Dropbox/ToolsForAnalytics/FinalProject/Lyrics/'
dataprep(folder)
print(1)
    


