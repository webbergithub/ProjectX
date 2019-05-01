# -*- coding: utf-8 -*-

#Data preprocessing into Dataframe 
#Include id, artist, title, lyrics columns
#Set id as index


def dataprep(folder):
    
    import glob
    import errno
    import pandas as pd
    
    if folder.endswith('/'):
        path = folder + '*.txt'
    else:
        path = folder + '/*.txt'
        
    files = glob.glob(path)
    #l is list for Lyrics
    l=list()
    # l1 is list for ID    
    l1=list()
    #l2 is list for Artist
    l2=list()
    #l3 is list for Song
    l3=list()
    #l4 is list for length
    l4=list()
    #l5 is list for love song
    l5=list()
    #l6 is list for mood
    l6=list()
    #l7 is list for not kid
    l7=list()
    #l8 is list for complexity
    l8=list()
    
    for name in files:
        try:
            with open(name) as fp:
                list_ = (name.split("/"))
                temp = list_[8]
                temp2 = temp.split('.')
                x=temp2[0]                
                count=0
                count1=0
                count2=0
                content = fp.read()
                l.append(content)
                l1.append(x.split('~')[0])
                l2.append(x.split('~')[1])
                l3.append(x.split('~')[::-1])
                l4.append(len(content.split()))
                for x in content.split():
                    #Using list of LWL Love Word List
                    if x.lower() in ['love','baby','feeling','loving','feel','touch','around','care','heart','mine']:
                        count+=1
                l5.append(count)
                for x in content.split():
                    #Using list of PWL Positive Word List
                    if x.lower() in ['good','nice']:
                        count1+=1
                l6.append(count1)
                        
                for x in content.split():
                    #Using list of SWL Swear Word List
                    if x.lower() in ['fuck','bitch','niggas','nigga','shit','death','died','dies','fucking','ass','motherfucking','bullshit','flesh','suck','sucking']:
                        count2+=1
                l7.append(count2)
                l8.append(len(set(content.split())))
                
                
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise  
                
                
    df=pd.DataFrame()
    df['ID']=l1
    df['Artist']=l2
    df['Song']=l3
    df['Lyrics']=l
    df['length']=l4
    df['love song']=l5
    df['mood']=l6
    df['not kid']=l7
    df['complexity']=l8
    
    
    #calculating scores
    df['song_length']=df['length']/df['length'].max()
    df[df['love song']==0]['love song'].count()
    df['song_love']=df['love song']/10
    l=list(df['love song'])
    len(df[df['song_love']>1])
    df[df['mood']>100]
    df['song_mood']=df['mood']/14
    len(df[df['song_mood']>1])
    df[df['not kid']>5]
    l=list()
    for x in df['song_mood']:
        if x>1:
            l.append(1)
        else:
            l.append(x)
    df['song_mood']=l
    l=list()
    for x in df['song_love']:
        if x>1:
            l.append(1)
        else:
            l.append(x)
            
    df['song_love']=l
    
    df['Lyrics'][577]
    len(df[df['not kid']>1])
    df1=df[['length','complexity']]
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df1=pd.DataFrame(scaler.fit_transform(df[['complexity','length']]))
    df['song_complexity']=df1[0]
    df['song_length']=df1[1]
    d=list()
    for x in df['Song']:
        d.append(x[:-4])
    df['Song']=d
    data=pd.DataFrame()
    data['id']=df['ID']
    data['artist']=df['Artist']
    data['song']=df['Song']
    data['kid_safe']=df['not kid']
    data['love']=df['song_love']
    data['mood']=df['song_mood']
    data['length']=df['song_length']
    data['complexity']=df['song_complexity']
    
    
    json_=data.to_json(orient='records')
    final=dict()
    
    final['characterizations']=json_
    
    
    
    
    
    return final
    
    
    
print('Enter your lyrics folder:')
#folder = input()
folder = '/Users/webbermb/Documents/Dropbox/ToolsForAnalytics/FinalProject/Lyrics/'
dataprep(folder)
print(1)
    


