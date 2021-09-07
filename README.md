# nlp-project-similar-lyrics

**About the project** <br>

The goal of my project is to find similar songs to a song with the NLP
methods. For now I worked with spacy for extracting repeating nouns and adjectives from 
lyrics, as well as with textblob for the sentiment analysis of lyrics. 
I plan to expand this project with new methods in the future.
For all methods I only consider the lyrics of the songs, and not other information like
the genre of the song.

I am working alone on this project and it is my project work for my university class
"Advanced Natural Language Processing with Python": https://esther.seyffarth.one/classes/2021-advanced-nlp/.


**The data**

For my project I created a corpus of lyrics which I cannot include do to copyright 
reasons. However, now follow instructions on how you can create a corpus for
this project yourself.
I created my corpus in XML and used https://genius.com/ as the source for the lyrics.
You can see how my corpus is structured in the corpus_example_structure.xml file.
Because I wanted to work with XML, it was the easiest way for me to just copy and paste
the lyrics and delete "Chorus", "Verse", "Bridge" etc., so that it is just one connected
text. I thought about using a web scrapper but since I wanted the exact structure you 
can see in the file, using it would have been more time-consuming.


**How you can try out the code yourself**

You can find all the packages I used for this project in the requirements.txt file which
you can install with the following command: pip install -r requirements.txt.
The linter I used is also included in the file in case you want to change and add to the code but keep the code style. I decided to follow Google's style and therefore used pylint.

I tried out three different methods to find similar songs. You can combine all of them
or only use one or two. First, I will explain how you work with all methods, for the
use of the single methods see below.

**All methods**

If you open the folder code, you will see eight files.
The module song_information.py is needed for all other files, so you might
want to open that first. The modules lyrics_adjectives.py, lyrics_sentiment.py
and lyrics_topics.py contain functions needed for the different approaches.
If you do not want to try out every method seperately but directly see the results
of all methods combined and compared, you should open all files and run the file results_combined.py. For the code it is necessary that you add the path to your corpus
and the path to the directory in which you want to save the results to the files topics_analysis.py, adjectives_analysis.py, sentiment_analysis.py and combined_results. You can easily find where you have to insert your path by searching for "PATH". You still need to comment in those lines.
If you run the file results_combined.py code you will export the data frames
with all results.
If you want to try out each method seperately first (recommended) and also use the query functions
with which you can for example get song recommendations for single songs or find songs
about a certain topic, you can also take a look at the next section where I explain how
to use each method independently.

**Single methods**

Find similar songs based on main topics 

This is the first method for finding similar and you need to open the file
topics_analysis.py and the modules song_information.py and lyrics_topics.py for this. 
These are all the files you need to
find similiar songs based on the same main topics. Check out the files for further explanations
and example queries. Do not forget to add the path to your corpus
and the path to the directory in which you want to save the results, to the file topics_analysis.
You can easily find where you have to insert your path by searching for "PATH". You still need to comment in those lines.
NLP method: extract main topics from a text with spacy 

Find similar songs based on repeating adjectives

This method is based on the first method and has similar but fewer functions. 
For this method you only need the modules song_information.py, lyrics_adjectives.py and the file adjectives_analysis. 
Check out the files for further explanations and example queries. 
Do not forget to add the path to your corpus and the path to the directory in 
which you want to save the results, to the file adjectives_analysis.
You can easily find where you have to insert your path by searching for "PATH". You still need to comment in those lines.
NLP method: extract repeating adjectives from a text with spacy 

Find similar songs based on the same sentiment 

This method differs from the other methods and uses sentiment analysis to find similar songs.
All the files you need for these method are sentiment_analysis.py and the modules
song_information.py and lyrics_sentiment.py. 
Check out the files for further explanations and example queries.
Do not forget to add the path to your corpus and the path to the directory in 
which you want to save the results, to the file sentiment_analysis.
You can easily find where you have to insert your path by searching for "PATH". You still need to comment in those lines.
NLP method: sentiment analysis with textblob

