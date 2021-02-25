# tt-stonks
##### Small program written in python allowing user to stream tweets* for given tickers, filter them and save important ones
*given of course that you have a (easily created) Twitter Developer Account


## How-to use

##### Setup and dependencies

``` 
git clone https://github.com/KrissKry/tt-stonks
cd tt-stonks
pip3 install playsound
pip3 install tweepy
```

##### Configuration
To work at all, as a user, you have to input your API_KEYs and SECRET_TOKENs in ```constants.py```. Without them, you will be unable to auth correctly with twitter api.
###### ```tickers.txt```
This file contains tickers that are tracked directly from twitter, and will be streamed to the user, they are not necessarily the same as categories in the next 2 files. I have supplied repo with my sample file. The takeaway is that every ticker should be separated by a coma and a blankspace for the program to parse it correctly. No symbol should be put at the end of the line. Another example of the file would be: 
```
dog, cat, woof
```


###### ```tweet_discard_phrases.txt```
This is where you put all words and phrases that should be labeled as spam and filtered out without printing to console or saving the tweet to file. The file's structure is a little different as you can supply the program with as many subcategories as you like. All phrases should be separated by a coma and a blankspace without any symbols at the end of the line. Remember not to leave any empty lines aswell.

- A new set of rules should begin in a new line with 3 underscores, keyword and another 3 underscores:
```___HUSKY___``` or ```___DOG___``` declare a new set of phrases that should be checked if that particular keyword is found in the tweet. 

- Under ```___GENERAL___``` as you might have guessed it, all general words and phrases are put that are common for all tickers.

[!] Please note that for now, the first keyword found in the tweet is used along ```___GENERAL___``` to spam check the content. Eg for tweets with text:
- 'a big fluffy husky dog', the program will use *GENERAL* and *HUSKY* rules,
- 'a big fluffy dog husky', the program will use *GENERAL* and *DOG* rules. 

It is a subject to further development.


###### ```tweet_keywords.txt```
Similarly to tweet_discard_phrases.txt this file has the same structure. ___It is crucial to have rules in the same order as in the previous file___, because as for now, single indexing is used to access phrases from both spam and importance string arrays.



#### Calculating tweet's importance
The way keywords work, is that the program evaluates tweet's importance / impact based on how many words from the dictionary it will find in the text, as well as, the account's followers count. For now printing to console requires one less point of importance than to save it to a file. 

[!] Please note that particular thresholds and environmental variables are a subject to further changes.


#### Tweaking program's usability and efficiency
Creating a correct dictionary for tweets is a rather cumbersome and time-consuming, but a necessary task to work with the program efficiently and have only useful tweets for analysis. Given the uniqueness of internet slang, the dictionary should be updated by it's user frequently.


#### Running the program
With api keys and tokens set, as well as tickers and thresholds tweaked, just launch the program with:
```
python3 main.py
```
Sit back, relax, enjoy.