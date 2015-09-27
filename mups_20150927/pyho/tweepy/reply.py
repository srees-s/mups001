'''
# auth get your keys from <https://docs.google.com/document/d/1ZtRuz5dRhUSUSLzNVjOCSCa_2Nm5W1bvsITFe1B8JfE/edit>
'''

import tweepy


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create and authenticated instance
api = tweepy.API(auth)

# get current user info
# this grabs a recent mentions from your timeline

meUser = api.mentions_timeline(count=1)

# Iterate through the list of mentions

for mention in meUser:
    # get the username mentioning you
    target = mention.user.screen_name
    
    #print target
    
    # put @ before the usern ame to formulate a reply
    target = '@' + target
    
    botSpeak = target + 'I\'m a bot and this text don\'t compute 2'
    
    api.update_status(status=botSpeak)
    
    break

    

