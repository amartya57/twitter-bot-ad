import json as _json
import random as _random

def _get_quotes():
    with open("quotes.json") as quotes_file:
        quotes=_json.load(quotes_file)
    return quotes

def _get_random_quote():
    quotes=_get_quotes()
    quote=_random.choice(quotes)
    
    return quote

def _form_tweet(quote):
    author = quote["author"].strip(",")
    quote_content=quote["quote"]
    if quote_content[0]!='“' :
        quote_content='“'+quote_content
    if quote_content[-1]!='”':
        quote_content=quote_content+'”'
    tweet = f'{quote_content} -- {author}'
    
    return tweet

def _is_valid_characters(tweet) :
    return len(tweet) <= 280

def get_tweet():
    while True :
        quote = _get_random_quote()
        tweet = _form_tweet(quote)
        if _is_valid_characters(tweet):
            return tweet
        
        
#print(get_tweet())
        