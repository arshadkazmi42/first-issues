## How to use
To use this bot, 
- Clone the repository
- Create a `credentials.json` in root directory and add the details from the twitter account, on which you want the bot to tweet.

```javascript
// credentials.json

{
  "Consumer Key": "TWITTER_CONSUMER_KEY",
  "Consumer Secret": "TWITTER_CONSUMER_SECRET",
  "Access Token": "TWITTER_APP_ACCESS_TOKEN",
  "Access Token Secret": "TWITTER_APP_TOKEN_SECRET",
  "Owner": "TWITTER_ACCOUNT_USERNAME",
  "Owner ID": "TWITTER_ACCOUNT_ID" // This should be an integer value
}

```

- Change the label which you want to fetch from github [here](https://github.com/arshadkazmi42/first-issues/blob/master/first_timers/first_timers.py#L11)
You can add your labels which ever you want this bot to fetch

- Finally to run execute the script, use below command
  - To only fetch the issues and store without tweeting

    ```
    python first_timers/run.py --creds-path credentials.json --db-path data/db.json --only-save
    ```

    This command will fetch all the issues with the defined label and it will be store in `data/db.json` file.

  - To fetch and tweet the issues use the below command

    ```
    python first_timers/run.py --creds-path credentials.json --db-path data/db.json
    ```

    This will fetch the issues with the defined label and store/update `data/db.json` and then tweet the issues which are not already there in `db.json`

This script will not tweet the fetched issues which are already exists in `db.json` store
