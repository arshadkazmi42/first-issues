.PHONY: clean-pyc init lint test install create-db fetch-issues tweet-issues


lint:
	flake8 --exclude=.tox


install:
	pip install -r requirements.txt


create-db:
	python first_timers/run.py --creds-path credentials.json --db-path data/db.json --only-save --create


fetch-issues:
	python first_timers/run.py --creds-path credentials.json --db-path data/db.json --only-save


tweet-issues:
	python first_timers/run.py --creds-path credentials.json --db-path data/db.json


test:
	pytest --verbose --color=yes $(TEST_PATH)


clean-pyc:
	echo "Cleaning, TBD"


