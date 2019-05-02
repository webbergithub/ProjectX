#!/usr/bin/env python
# coding: utf-8

# In[31]:


# %load usingintersect.py

#Data preprocessing into Dataframe 
#Include id, artist, title, lyrics columns
#Set id as index
SWL=[
     'anal',
     'anus',
     'arse',
     'ass',
     'ballsack',
     'balls',
     'bastard',
     'bitch',
     'biatch',
     'bloody',
     'blowjob',
     'blow',
     'job',
     'bollock',
     'bollok',
     'boner',
     'boob',
     'bugger',
     'bum',
     'butt',
     'buttplug',
     'clitoris',
     'cock',
     'coon',
     'crap',
     'cunt',
     'damn',
     'dick',
     'dildo',
     'dyke',
     'fag',
     'feck',
     'fellate',
     'fellatio',
     'felching',
     'fuck',
     'f',
     'u',
     'c',
     'k',
     'fudgepacker',
     'fudge',
     'packer',
     'flange',
     'Goddamn',
     'God',
     'damn',
     'hell',
     'homo',
     'jerk',
     'jizz',
     'knobend',
     'knob',
     'end',
     'labia',
     'lmao',
     'lmfao',
     'muff',
     'nigger',
     'nigga',
     'omg',
     'penis',
     'piss',
     'poop',
     'prick',
     'pube',
     'pussy',
     'queer',
     'scrotum',
     'sex',
     'shit',
     's',
     'hit',
     'sh1t',
     'slut',
     'smegma',
     'spunk',
     'tit',
     'tosser',
     'turd',
     'twat',
     'vagina',
     'wank',
     'whore',
     'wtf'
     ]

LWL=[
     'love',
     'like',
     'time',
     'right',
     'good',
     'well',
     'world',
     'long',
     'around',
     'sweet',
     'mind',
     'better',
     'light',
     'new',
     'hard',
     'made',
     'enough',
     'stars',
     'high',
     'run',
     'looking',
     'rock',
     'best',
     'shine',
     'god',
     'free',
     'happy',
     'hot',
     'fine',
     'heaven',
     'loved',
     'smile',
     'hands',
     'pretty',
     'strong',
     'pain',
     'easy',
     'dead',
     'work',
     'use',
     'loves',
     'beautiful',
     'gold',
     'first',
     'darling',
     'loving',
     'top',
     'ready',
     'non',
     'low',
     'fun',
     'wonder',
     'angel',
     'great',
     'bright',
     'star',
     'lovely',
     'catch',
     'warm',
     'glad',
     'trouble',
     'eye',
     'known',
     'celebrate',
     'boom',
     'nice',
     'golden',
     'win',
     'send',
     'rich',
     'lover',
     'whoa',
     'promise',
     'cut',
     'clear',
     'magic',
     'sweetheart',
     'peace',
     'grace',
     'trust',
     'fast',
     'lucky',
     'lead',
     'everlasting',
     'dawn',
     'thank',
     'thrill',
     'brand',
     'luck',
     'cool',
     'miracle',
     'perfect',
     'state',
     'problem',
     'pleasure',
     'grand',
     'smiling',
     'worth',
     'tough',
     'setting'
     ]

NWL=[
     'like',
     'get',
     'time',
     'one',
     'back',
     'little',
     'life',
     'long',
     'us',
     'un',
     'bad',
     'head',
     'left',
     'die',
     'cry',
     'wrong',
     'hard',
     'last',
     'two',
     'lost',
     'fall',
     'shit',
     'high',
     'far',
     'run',
     'lonely',
     'set',
     'break',
     'used',
     'god',
     'sin',
     'white',
     'crazy',
     'na',
     'happy',
     'lose',
     'cold',
     'fuck',
     'bust',
     'hit',
     'burning',
     'pain',
     'bitch',
     'dead',
     'lies',
     'falling',
     'sad',
     'shake',
     'tricky',
     'lie',
     'dark',
     'ding',
     'wild',
     'top',
     'funny',
     'knock',
     'broken',
     'line',
     'non',
     'low',
     'yet',
     'blow',
     'burn',
     'water',
     'war',
     'poor',
     'hurt',
     'sugar',
     'fool',
     'drop',
     'hell',
     'fear',
     'ho',
     'full',
     'hate',
     'trouble',
     'known',
     'broke',
     'damn',
     'hang',
     'tired',
     'miss',
     'blind',
     'rich',
     'fell',
     'sick',
     '2',
     'strange',
     'loose',
     'freeze',
     'fever',
     'smell',
     'worry',
     'smoke',
     'afraid',
     'pretend',
     'died',
     'mad',
     'blame',
     'kill',
     'shame',
     'slowly',
     'lying',
     'devil',
     'mystery',
     'scream',
     'fucking',
     'second',
     'refuse',
     'wood',
     'mistakes',
     'tout',
     'burns',
     'steal',
     'bastards',
     'hurts',
     'problem',
     'breaking',
     'scared',
     'troubles',
     'fears',
     'moving',
     'fake',
     'dying',
     'foolish',
     'less',
     'death',
     'loud',
     'mess',
     'job',
     'dirt',
     'slow',
     'twist',
     'weed',
     'evil',
     'dick',
     'weak',
     'problems',
     'killing',
     'deny',
     'crowded',
     'cash',
     'bleed',
     'gutter',
     'rough',
     'crime',
     'bum',
     'losing',
     'dumb',
     'drain',
     'sorry',
     'mar',
     'fat',
     'trick',
     'stuck',
     'lame',
     'breaks',
     'revenge',
     'crack',
     'heavy',
     'missed',
     'giddy',
     'suffer',
     'beg',
     'self',
     'cat',
     'dust',
     'silly',
     'confess',
     'impossible',
     'punk',
     'shady',
     'misery',
     'drag',
     'sorrow',
     'waste',
     'liar',
     'desert',
     'dope',
     'awful',
     'buzzing',
     'gasp',
     'dirty',
     'struggle',
     'vain',
     'freak',
     'lonesome',
     'american',
     'slave',
     'lived',
     'curse',
     'slaves',
     'twisted',
     'grind',
     'doubt',
     'lied',
     'risk',
     'ashamed',
     'wicked',
     'laid'
     ]

def dataprep(folder):
    
   
    import pandas as pd
    import os
    lyrics=list()
    import glob, os
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
    LWL_set = set(LWL)
    NWL_set = set(NWL)
    SWL_set = set(SWL)
    
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
                
                
    df=pd.DataFrame()
    df['id']=l1
    df['artist']=l2
    df['song']=l3
    df['Lyrics']=l
    df['length']=l4
    df['love song']=l5
    df['mood']=l6
    df['not kid']=l7
    df['complexity']=l8
    #print(df)
    
    #calculating scores
    df['length']=df['length']/(df['length'].max()-df['length'].min())
    df['love']=df['love song']/(df['love song'].max()-df['love song'].min())
    df['mood']=df['mood']/(df['mood'].max()-df['mood'].min())
    df['kid_safe']=df['not kid']/(df['not kid'].max()-df['not kid'].min())
    df['complexity']=df['complexity']/(df['complexity'].max()-df['complexity'].min())
    for x in df['song']:
        d.append(x[:-4])
    df['song']=d
    df=df.drop(columns='Lyrics')

    
    
    json_=df.to_json(orient='records')
    final=dict()
    
    final['characterizations']=json_
    print(final)

    
    
    
    
    
    return final
    
    
if __name__ == '__main__':  
    
    
    
    #print('Enter your lyrics folder:')
#     folder = 'C:/Users/Ankita Bhardwaj/Downloads/Lyrics'
#     #folder = '/Users/webbermb/Documents/Dropbox/ToolsForAnalytics/FinalProject/Lyrics/'
#     dataprep(folder)
    
    import argparse

    parser = argparse.ArgumentParser(description='path to directory of the folder with lyric files')
    parser.add_argument('file')
    args = parser.parse_args()

    dataprep(args.file)
    
    print(1)
    