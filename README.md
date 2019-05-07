#Group name: groupX

# ProjectX in Tools For Analytics

Project X is a final project for a course in Columbia, ToolsForAnalytics. The team members are:
    a. Webber Hsu (hh2750)
    b. Ankita Bhardwaj (ab4685)
We are designing a scoring system to lyrics analyzing aspects such as length, complexity and etc. 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install several packages using in the code. 
    a. errno
    b. os
    c. pandas
    d. glob
```    
Example:
-->bash

pip install glob
```

## Usage (Functions in 'main.py')

The program can take in a definite path of foler holding lyrics in txt files.
It can be executable as a single command. 
The input to your command should be the path to the directory holding the song files. 
The output of your command should be a JSON object (sent to standard out, StdOut) that contains a list of characterizations; one for each song. 
Each characterization object should have the listed dimensions (keys) and a values for how well the song fits into that dimension. 

Dimensions
    kid_safe: no bad words
        0 is not kid safe
        1 is very kid safe
    love: is it a love song? 
        0 is not a love song
        1 is a love song
    mood: Upbeat, has a positive message
        0 is a dark song
        1 is a very happy song
    length: how long is it
        0 is a short song
        1 is a very long song
    complexity: requires high level of vocabulary to understand
        0 is a very simple song: https://www.youtube.com/watch?v=EdMTl9zHQ9Y
        1 is a very complex song
        
## Code Logics

1. importing lyrics and selected word lists
2. token analysis in kid_safe, love, mood dimension
3. counting length of the song for lenght dimension
4. counting unique words for complexity dimension
5. normalization by the max of each counts
6. save as a json file with required format
7. PROJECT DONE MIC DROP 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

