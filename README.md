# interview-alexa-skill
Amazon Alexa skill for 'Interview With Alexa' conference talk

# to test
source env/bin/activate
py.test tests/test_handler.py

# to create

* add a new repo in github
* clone it locally

* install Serverless
```
$ npm install -g serverless
$ serverless create --template aws-python
```

* update serverless.yml

** changed the service name

** set the environment to python 3, in Europe zone
```
provider:
  name: aws
  runtime: python3.6
  stage: dev
  region: eu-west-1
```

copied in my standard handler.py, intents.json,
copied requirements.txt + tests folder + __init__.py, conftest.py, mock_alexa.py, test_handler.py
exluded them all in serverless.yml

* used a python virtual environment
```
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ py.test tests/test_handler.py
```

* deployed the Lambda function via Serverless
```
$ sls deploy
```

* created a new Alexa Skill with language English (U.K.)
* named it 'interview'
* added the interaction model (didn't use the builder as it insisted on submitting for testing!)
* configured it with the ARN from the Lambda function
