import tweepy
import time
#insert your Twitter keys here
#html50
#
consumer_key ='0LuTrRREENED9pcmsFZCk7quR'
consumer_secret='sZK8gVABppe2HwaOpiSkORSTphnaeMmLZOTmmADoW33Br2Fykx'
access_token='3273108757-jkBK4uhDelfmNz4AOF6FsLf4CWqzAyfiqH05I8O'
access_secret='kBZX2CBzO6Kr8QLIcvJ7MxyBqMjeeDfcRlQOTIsma7wSp'
 
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
 
list= open('C:\Users\Leonardo\Desktop\html5.txt','w')
 
if(api.verify_credentials):
    print 'We sucessfully logged in'
 
user = tweepy.Cursor(api.followers, screen_name="html5").items()
 
while True:
    try:
        u = next(user)
        list.write(u.screen_name +' \n')
 
    except:
        time.sleep(15*60)
        print 'We got a timeout ... Sleeping for 15 minutes'
        u = next(user)
        list.write(u.screen_name +' \n')
list.close()
