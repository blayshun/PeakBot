# PeakBot is an automated bot designed to respond to incorrect uses of "sneak peek" when the user uses "peak" instead.
# this bot will utilize the Tweepy library
import tweepy
import time     # utilized to pause the bot and refresh every ten minutes

# Credentials -------------------------------------------------------------------------------------------------------

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# -------------------------------------------------------------------------------------------------------------------

# Begin process of searching through tweets using a specific keyword
def search_and_respond():

    search = '"sneak peak"' # the phrase the bot will be correcting

    response = '''

    Peak – (noun) the pointed top of a mountain.; (verb) to reach a highest point ; (adj.) maximum

    Peek – (noun) a quick or furtive look; (verb) look quickly

    I'm sure you didn't mean to sneak the top of a mountain anywhere.
    '''

    retrievetweets = 15 # the number of tweets the bot will be interacting with

    user_history = [] # keeps a list of usernames to ensure the bot does not spam users

    # Begin iteration of searched tweets
    for tweet in tweepy.Cursor(api.search, search).items(retrievetweets):
        try:
            tweetID = tweet.user.id
            username = tweet.user.screen_name
            test_user = username.lower()    # creates a formatted string of 'username' to test in [user_history]
            if test_user in user_history:
                continue                    # continues iteration if a user in [user_history] is matched
            else: api.update_status("@" + username + " " + response, in_reply_to_status_id = tweetID)
            print("Successfully informed the user @" + username)    # else, responds to the user
            user_history.append(test_user)   # appends 'username' to [user_history] to prevent repeats

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

while True:
    search_and_respond()
    time.sleep(600)    # the bot will pause and refresh every ten minutes
