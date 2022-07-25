import os as _os
import dotenv as _dotenv
import time as _time
import tweepy as _tweepy

import services as _services
import unsplash as _unsplash

_dotenv.load_dotenv()


API_KEY=_os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET_KEY"]
ACCESS_TOKEN=_os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET=_os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

def _get_twitter_api():
    auth=_tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api=_tweepy.API(
        auth,
        wait_on_rate_limit=True
    )
    
    return twitter_api

def _write_tweet():
    tweet=_services.get_tweet()
    twitter_api=_get_twitter_api()
    twitter_api.update_status(tweet)
    
def _post_image():
    _unsplash.download_image()
    tweet=_services.get_tweet()
    twitter_api=_get_twitter_api()
    twitter_api.update_status_with_media(tweet, "picture.jpg")
    
def run():
    while True:
        _post_image()
        #_time.sleep(60) #testing
        _time.sleep(43200)
        
if __name__=="__main__":
    run()
    
#_post_image()
# _write_tweet()