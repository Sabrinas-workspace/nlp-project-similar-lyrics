# nlp-project-similar-songtexts

**About the project**

The goal of my project is to find similar songs to a song with different NLP
methods. For this I only consider the songtext of the songs.
For now I worked with spacy for extracting repeating nouns and adjectives from a
songtext, as well as with textblob for the sentiment analysis of a songtext. 
I plan to expand this project with new methods in the future.

I am working alone on this project and it is my project work for my university class
"Advanced Natural Language Processing with Python": https://esther.seyffarth.one/classes/2021-advanced-nlp/.


**The data**

For my project I created a corpus of songtexts which I cannot include do to copyright 
reasons. However, now will follow instructions on how you can create a corpus for
this project yourself.
I created my corpus in XML and used https://genius.com/ as source for the songtexts.
You can see how my corpus is structured in the corpus_example_structure.xml file.
Because I wanted to work with XML, it was the easiest way for me to just copy and paste
the songtexts and delete "Chorus", "Verse", "Bridge" etc., so that it is just one connected
text. I thought about using a web scrapper but since I wanted that exact structure you 
can see in the file, using it would have been more time-consuming.


**How you can try out the code yourself**

You can find all the packages I used for this project in the requirements.txt file.
There is also the linter I used included, in case you want to change and add to the code
but keep the code style. I decided to follow Google's style and therefore used pylint.

I tried out three different methods to find similar songs. You can combine all of them
or only use one or two. First, I will explain how you work with all methods, for the
use of the single methods see below.

**All methods**

If you open the folder code, you will see four modules and four folders.
The module song_information.py is needed for all other three modules, so you might
want to open that first. The modules songtext_adjectives.py, songtext_sentiment.py
and songtext_topics.py contain functions needed for the different approaches.
If you do not want to try out every method seperately but directly see the results
of all methods combined and compared, you should open the folder results_for_all_methods_combined
in which you find the results.py file. If you run this code you will get the dataframes
with all results.
If you want to try out all methods seperately first (recommended) and also use the query functions
with which you can for example get song recommendations for single songs or find songs
about a certain topic, you can also take a look at the next section where I explain how
to use the methods independently.

**Single methods**

find_similar_songs_based_on_main_topics 

This is the first method for finding similar_songs and also a folder in which find
the topics_analysis.py file which you need for this. You also need the modules 
song_information.py and songtext_topics.py. These are all the files you need to
find similiar songs based on the same main topics. Check out the files for further explanations
and example queries.
NLP method: extract main topics from a text with spacy 

find_similar_songs_based_on_adjectives

This method is based on the first method and has similar but fewer functions. 
In this folder you can find the adjectives_analysis.py file which you need for this
method. Furthermore you need the modules song_information.py and songtext_adjectives.py. 
These are all the files you need to find similiar songs based on common adjectives. 
Check out the files for further explanations and example queries.
NLP method: extract repeating adjectives from a text with spacy 

find_similar_songs_based_on_sentiment 

This is a more different method and in the folder you can find the file
sentiment_analysis.py which you need for this. In addition you need the modules
song_information.py and songtext_sentiment.py. 
These are all the files you need to find similiar songs based on the same sentiment. 
Check out the files for further explanations and example queries.
NLP method: sentiment analysis with textblob

