## DOCKER DEPLOYMENT

- Clone the repository
- Go to project root directory
  ```
    cd first-issues
  ```
- Build image using this command
  ```
    docker build -t firstissuescron .
  ```
- Create `credentials.json` file (read more about this in [HOW TO USE](HOW_TO_USE.md))
- Create container using this command
  ```
    docker run -t -i --mount type=bind,src={CREDENTIALS_PATH},dst=/home/first-issues/credentials.json --name firstissuescron firstissuescron
  ```
- Restart container

> **{CREDENTAILS_PATH}**: Absolute path for `credentails.json`
