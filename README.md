# interview-alexa-skill
Amazon Alexa skill for 'Interview With Alexa' conference talk

# to test
py.test tests/test_handler.py

# to create

* created a new repo in github
* cloned it locally
$ npm install -g serverless
$ serverless create --template aws-python
* updated serverless.yml
** changed the service name
** changed the runtime: to python3.6
** set   stage: dev
** set   region: eu-west-1

copied in my standard handler.py, intents.json,
copied requirements.txt + tests folder + __init__.py, conftest.py, mock_alexa.py, test_handler.py
exluded them all in serverless.yml

$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ py.test tests/test_handler.py

$ sls deploy
this created a new Alexa Skill with language English (U.K.), called 'interview' 2.5 kB
