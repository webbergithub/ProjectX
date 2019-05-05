
SWL_set = set(line.strip() for line in open('SwearWordList.txt'))
NWL_set = set(line.strip() for line in open('NegativeWordsList.txt'))
LWL_set = set(line.strip() for line in open('LoveWordsList.txt'))

def length(lyrics_content):
    return len((lyrics_content.split()))

def love_song(lyrics_content,keywords):
    return len(keywords.intersection(lyrics_content.split()))

def mood(lyrics_content,keywords):
    return len(keywords.intersection(lyrics_content.split()))

def kid_safe(lyrics_content,keywords):
    return len(keywords.intersection(lyrics_content.split()))

def complexity(lyrics_content):
    return len(set(lyrics_content.split()))

def dataprep(folder):
   
    import pandas as pd
    import os
    import glob
    os.chdir(folder)
    lyrics=list()
    for file in glob.glob("*.txt"):
        lyrics.append(file)
    

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
    d=list()
    
    for name in lyrics:
        try:
            with open(name,encoding="utf8") as fp:
                content = fp.read().lower()
                
               
                count=0
                count1=0
                count2=0
                
                l.append(content)
                l1.append(name.split('~')[0])
                l2.append(name.split('~')[1])
                l3.append(name.split('~')[-1])
                a=length(content)
                l4.append(a)
                
                
                #Calculating # of words for love song 
                #using intersection of love word set and lyrics word set
                
                count = love_song(content,LWL_set)
                l5.append(count)
                
                #Calculating # of words for mood
                #using intersection of love word set and lyrics word set
                count1 = mood(content,NWL_set)
                l6.append(count1)
                
                
                #Calculating # of words for love song 
                #using intersection of love word set and lyrics word set
                
                count2 = kid_safe(content,SWL_set)
                l7.append(count2)
                
                l8.append(complexity(content))

                
        except:
            raise  
    lis=list()            
    for i in l1:
        if i!='000':
            lis.append(i.lstrip('0'))
        else:
            lis.append(0)
            
    lis2=list()
    for i in l2:
        lis2.append(i.replace('-',' '))
    
    lis3=list()
    for i in l3:
        lis3.append(i.replace('-',' '))
            
    df=pd.DataFrame()   #storing as a dataframe
    df['id']=lis
    df['artist']=lis2
    df['song']=lis3
    df['Lyrics']=l
    df['length']=l4
    df['love song']=l5
    df['mood']=l6
    df['not kid']=l7
    df['complexity']=l8
    #print(df)
    
    

    
    #calculating scores
    df['length']=df['length']/(df['length'].max())
    df['love']=df['love song']/(df['love song'].max())
    df['mood']=df['mood']/(df['mood'].max())
    df['kid_safe']=df['not kid']/(df['not kid'].max())
    df['complexity']=df['complexity']/(df['complexity'].max())
    for x in df['song']:
        d.append(x[:-4])
    df['title']=d
    df=df.drop(columns=['Lyrics','love song','not kid','song'])
    
    data=pd.DataFrame() #storing in a right format
    data['id']=df['id']
    data['artist']=df['artist']
    data['title']=df['title']
    data['kid_safe']=1-df['kid_safe'] # For changing the maximum value to be the most kid safe
    data['love']=df['love']
    data['mood']=1-df['mood'] # For changing the maximum value to be of the most happy song
    data['length']=df['length']
    data['complexity']=df['complexity']
    
    l=list()
    for x in range(len(data)):  #creating a list of dictionaries
        d=dict()
        d['id']=int(data['id'][x])
        d['artist']=data['artist'][x]
        d['title']=data['title'][x]
        d['kid_safe']=data['kid_safe'][x]
        d['love']=data['love'][x]
        d['mood']=data['mood'][x]
        d['length']=data['length'][x]
        d['complexity']=data['complexity'][x]
        l.append(d)
        
    final=dict()
    
    final['characterizations']=l
    #final=json.dumps(final)
       
    
    
    return final
    
    
if __name__ == '__main__':  
    
    import json
    import argparse
    parser = argparse.ArgumentParser(description='path to directory of the folder with lyric files')
    parser.add_argument('file')
    args = parser.parse_args()
    data=dataprep(args.file)
    with open('CSV-JSON-lyrics-out.json', 'w') as fp:
        json.dump(
            obj=data,
            fp=fp,
            indent=True,  # pretty printing
            #sort_keys=True,  # sorting for easier lookup by a human, sort alphebetically
        )
    with open('CSV-JSON-lyrics-out.json','r') as fp:
        print_data = json.load(fp)
    
        print(print_data)



