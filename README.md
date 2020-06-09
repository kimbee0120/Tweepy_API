# Tweepy_API
*Twitter provides an API that you can download twitter tweets data*
https://developer.twitter.com/en
- You need to request an access token 

## Step 1
<li> Create variables that contains the user credentials to access twitter API </li>

```Python
access_token = "your consumer key"
access_token_secret = "your consumer secret"
consumer_key = "your access token"
consumer_secret = "your access token secret"
```

## Step2
<li> Create Twitter authetification and the connection to Twitter Straming API</li>

```Python
if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Cyber Security', 'Stock', 'Software Engineer'])


```
## Step3
<li> Create Calling Twitter Streaming Python Program and run the program to save data.</li>
- this program will be called automatically with cron to run every 2 hrs.