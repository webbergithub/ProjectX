
#Loading List of token in different aspects 
SWL_set = set(line.strip() for line in open('SwearWordList.txt'))
NWL_set = set(line.strip() for line in open('NegativeWordsList.txt'))
LWL_set = set(line.strip() for line in open('LoveWordsList.txt'))

def dataprep(folder):
    
   
    import pandas as pd
    import os
    import glob
    import errno
    lyrics=list()
    os.chdir(folder)
    for file in glob.glob("*.txt"):
        lyrics.append(file)
#    print(lyrics)
    
#     if folder.endswith('/'):
#         path = folder + '*.txt'
#     else:
#         path = folder + '/*.txt'
#     print(path)
        
#     files = glob.glob(path)


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
                content = fp.read()

#                 list_ = (name.split("/"))
#                 temp = list_[8]
#                 temp2 = temp.split('.')
#                 x=temp2[0]                
                count=0
                count1=0
                count2=0
                
                l.append(content)
                l1.append(name.split('~')[0])
                l2.append(name.split('~')[1])
                l3.append(name.split('~')[-1])
                l4.append(len(content.split()))
                
                lyrics_set = (content.split())
                
                #Calculating # of words for love song 
                #using intersection of love word set and lyrics word set
                
                count = len(LWL_set.intersection(lyrics_set))
                l5.append(count)
                
                #Calculating # of words for mood
                #using intersection of love word set and lyrics word set
                count1 = len(NWL_set.intersection(lyrics_set))
                l6.append(count1)
                
                
                #Calculating # of words for love song 
                #using intersection of love word set and lyrics word set
                
                count2 = len(SWL_set.intersection(lyrics_set))
                l7.append(count2)
                
                l8.append(len(set(content.split())))
                #print(len(l1))
#                 print(len(l2))
#                 print(len(l3))
#                 print(len(l4))
#                 print(len(l5))
#                 print(len(l6))
#                 print(len(l7))
#                 print(len(l8))
                
        except IOError as exc:
            if exc.errno != errno.EISDIR:
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
            
    df=pd.DataFrame()
    df['id']=lis
    df['artist']=lis2
    df['song']=l3
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
    df['song']=d
    df=df.drop(columns=['Lyrics','love song','not kid'])
    
    
    json_=df.to_json(orient='records')
    final=dict()
    
    final['characterizations']=json_
    #print(final)

    
    
    
    
    
    return final
    
    
if __name__ == '__main__':  
    
    
    
    #print('Enter your lyrics folder:')
     folder = 'C:/Users/Ankita Bhardwaj/Downloads/Lyrics'
#     #folder = '/Users/webbermb/Documents/Dropbox/ToolsForAnalytics/FinalProject/Lyrics/'
     data=dataprep(folder)
     print(data)
    
#     import argparse

#     parser = argparse.ArgumentParser(description='path to directory of the folder with lyric files')
#     parser.add_argument('file')
#     args = parser.parse_args()

#     dataprep(args.file)
    
    #print(1)
    



# In[ ]:





# In[ ]:





# In[ ]:




