###  How to use

To use this bot,

- Clone the repository. [Steps to clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository).
- Create a `credentials.json` in root directory and add the details from the twitter account, on which you want the bot to tweet.

```
// credentials.json

{ 
"Consumer Key":"TWITTER_CONSUMER_KEY", 
"Consumer Secret":"TWITTER_CONSUMER_SECRET",
"Access Token":"TWITTER_APP_ACCESS_TOKEN", 
"Access Token Secret":"TWITTER_APP_TOKEN_SECRET", 
"Owner":"TWITTER_ACCOUNT_USERNAME", 
"Owner ID":"TWITTER_ACCOUNT_ID" // This should be an integer value 
 }
 ```

Dont't know what these stand for? No problem, following are the steps. 

- Create a developer account in twitter and then create an app [here](https://developer.twitter.com/en/apps) which will give the following:
  - TWITTER_CONSUMER_KEY, 
  - TWITTER_CONSUMER_SECRET, 
  - TWITTER_APP_ACCESS_TOKEN, 
  - TWITTER_APP_TOKEN_SECRET

- TWITTER_ACCOUNT_USERNAME can be found out by logging in to [Twitter](https://twitter.com) and clicking on profile.  
 
- TWITTER_ACCOUNT_ID can be found out [here](http://gettwitterid.com/).

- Change the label name to the issue label which you want to fetch from github [here](https://github.com/arshadkazmi42/first-issues/blob/master/first_timers/first_timers.py#L11). 
- Finally to execute the script, use below command on command prompt
    - To only fetch the issues and store without tweeting

      ```
      python first_timers/run.py --creds-path credentials.json --db-path data/db.json --only-save
      ```
      
      This command will fetch all the issues with the defined label and it will be store in `data/db.json` file. 
    
    - To fetch and tweet the issues use the below command

        ``` 
        python first_timers/run.py --creds-path credentials.json --db-path data/db.json
        ```
        This will fetch the issues with the defined label and store/update `data/db.json` and then tweet the issues which are not already there in `db.json`.

This script will not tweet the fetched issues which already exists in `db.json` store
