# interview-alexa-skill
Amazon Alexa skill for 'Interview With Alexa' conference talk

# to test
source env/bin/activate
py.test tests/test_handler.py

# to create
## git
* add a new repo in github
* clone it locally

## Serverless
install
```
$ npm install -g serverless
$ serverless create --template aws-python
```

update serverless.yml with the service name, set the environment to python 3, locate in Europe zone
```
service: interview

provider:
  name: aws
  runtime: python3.6
  stage: dev
  region: eu-west-1
```

## starter code and tests
copied in my standard handler.py, intents.json,
copied requirements.txt + tests folder + __init__.py, conftest.py, mock_alexa.py, test_handler.py
exluded them (and just everything bar handler.py) in serverless.yml
```
package:
  exclude:
    - __pycache__/**
    - .cache/**
    - env/**
    - tests/**
    - handler.pyc
    - intents.json
    - LICENSE
    - policy.json
    - list_of_foods.txt
    - README.md
    - requirements.txt
    - sample_utterances.txt
```

## python (for testing)
* used a python virtual environment
```
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ py.test tests/test_handler.py
```

## deployment
* deployed the Lambda function via Serverless
```
$ sls deploy
```

## Alexa skill
* created a new Alexa Skill with language English (U.K.)
* named it 'interview'
* added the interaction model (didn't use the builder as it insisted on submitting for testing!)
* configured it with the ARN from the Lambda function
