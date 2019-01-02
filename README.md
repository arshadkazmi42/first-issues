# Good First Issues Bot :robot:

Bot which tweets all github issues, which are has `good first isse` label.
This is inspired by [Utkarsh's](https://github.com/musically-ut) work on [first-timers-only-bot](https://github.com/musically-ut/first-timers-only-bot)

You can follow the twitter account here [@first_issues](https://twitter.com/first_issues)

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

## Contributing

We are constantly working on improving this script and would love to get any types of contributions.
If you have got any suggestions, drop your suggestion [here](https://github.com/arshadkazmi42/first-issues/issues/new).
If you want to fix some existing bugs in the script, you can find open issues [here](https://github.com/arshadkazmi42/first-issues/issues)

We are also working on building a contributing guide.

## Supporters

[![Utkarsh Upadhyay ](https://github.com/musically-ut.png?size=100)](https://github.com/musically-ut) |
| --- |
[Utkarsh Upadhyay ](https://github.com/musically-ut) 


<a href="https://www.patreon.com/bePatron?u=15454240" target="_blank"><img src="https://c5.patreon.com/external/logo/become_a_patron_button.png" alt="Become a Patron!" height="41"></a>

Please consider donating, to keep our servers up and running 
