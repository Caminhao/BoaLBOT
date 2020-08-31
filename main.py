import tweepy
import time
from random import seed
from random import randint

CONSUMER_KEY = 'kliltnAtiQPs1wOdxAHyI89tN'
CONSUMER_SECRET = 'pvq0PSXInnmDj236Q66Os1B87lOPsbItCviuvJjLu362oGPJXa'
ACCESS_KEY = '1081381323653201920-tOmqtFGM80eYTLePGzsJvgwNs9dbD5'
ACCESS_SECRET = 'gy9Y5L83uvJhzBof3PF8qbV4DUJboEe33OIRKft6YkeEq'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
user = api.me()
print(user.name)
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone that is following " + user.name)


def mainfunction():
    search = "from:Ellygopain"
    numberoftweets = 79
    for tweet in tweepy.Cursor(api.search, search).items(numberoftweets):
        try:
            tweet.favorite()
            print('liked the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

    phrase = ["Muito boa essa kkkkkkkkkkkkk", "Esse L é muito espoleta hahahahaha",
              "Essa foi muito engraçada kkkkk", "Me mato de rir com esse menino gente ashuashuashuashuasahusahu",
              "Hahahahahaha", "KKKKKKKKKK", "hahahah", "kkkkkk", "haha", "hihihihihi", "kakakakakdkkakaka",
              "Hahahahahahahahahahahahahahaha", "hahahahah", "hahahahahahah", "boa boa hahahaha",
              "kkkkkkkk", "hahaha", "hahahahahahahha", "kkkkkkkkkkk", "HAHAHAHAHAHAH BOA", "KKKKKKK BOAA",
              "Essa aí foi boa mesmo hahahahah"]
    seed(1)
    for tweet in tweepy.Cursor(api.search, search).items(numberoftweets):
        value = randint(0, 21)
        try:
            tweetid = tweet.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase[value], in_reply_to_status_id=tweetid,
                              auto_populate_reply_metadata=True)
            print("Replied with " + phrase[value])
        except tweepy.TweepError as e:
            print(e.reason)


while True:
    mainfunction()
    time.sleep(300)
