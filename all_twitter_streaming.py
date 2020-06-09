#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[''])



# Bounding boxes for geolocations
# Online-Tool to create boxes (c+p as raw CSV): http://boundingbox.klokantech.com/
#    GEOBOX_WORLD = [-180,-90,180,90]
#    GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
#    GEOBOX_NJ_TRI_STATE = [-76.02767567429771,41.747798988721655, -71.5013084867977,38.74663700338296]
#    GEOBOX_KEAN = [-74.23984383798017,40.688051380918665,-74.22593926644697,40.673536322136094]


#   #stream.filter(locations=[-74.23984383798017,40.688051380918665,-74.22593926644697,40.673536322136094])

#    #NYC box longitude,latitude, longitude,latitude
#    stream.filter(locations=[-74.1687,40.5722,-73.8062,40.9467])

