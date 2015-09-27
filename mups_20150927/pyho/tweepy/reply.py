# auth get your keys from <https://docs.google.com/document/d/1ZtRuz5dRhUSUSLzNVjOCSCa_2Nm5W1bvsITFe1B8JfE/edit>
'''
Application Settings
Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
Consumer Key (API Key)    XZISR9sO8PYBlURR1KTRUziqQ
Consumer Secret (API Secret)    NzBBCZKReJ8WPDUIYWr0QuvdSMwhOU5wiZT49vTqPkCjGobqLn
Access Level    Read and write (modify app permissions)
Owner    SSreesankar
Owner ID    1134606306


Your Access Token
This access token can be used to make API requests on your own account's behalf. Do not share your access token secret with anyone.
Access Token    1134606306-qM7WJ84Wku1E0VHuXmZ9mFKZXXggiJGRVudmIdC
Access Token Secret    8zB7gNGj30nWymrKodEdHSJoGFnjGxFrrtmqObVpp06Jn
Access Level    Read and write
Owner    SSreesankar
Owner ID    1134606306

'''

import tweepy


consumer_key = "XZISR9sO8PYBlURR1KTRUziqQ"
consumer_secret = "NzBBCZKReJ8WPDUIYWr0QuvdSMwhOU5wiZT49vTqPkCjGobqLn"
access_token = "1134606306-qM7WJ84Wku1E0VHuXmZ9mFKZXXggiJGRVudmIdC"
access_token_secret = "8zB7gNGj30nWymrKodEdHSJoGFnjGxFrrtmqObVpp06Jn"


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

    

