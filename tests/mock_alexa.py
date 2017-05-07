import re

class MockAlexa(object):
    """A pretend Alexa.
    """

    def __init__(self, name, handler):
        self.name = name
        self.handler = handler
        self.active = False


    def activate(self):
        if self.active:
            new_session = False
        else:
            self.active = True
            new_session = True
        return new_session


    def ask_text(self, words):
        service_response = self.ask(words)
        text = service_response["response"]["outputSpeech"]["text"]
        return text


    def ask(self, words):
        new_session = self.activate()
        intent_name = None
        slots = None
        request_type = ""
        if "open {}".format(self.name) in words:
            request_type = "LaunchRequest"
        if "help".format(self.name) in words:
            request_type = "IntentRequest"
            intent_name = "AMAZON.HelpIntent"
        if "exit".format(self.name) in words:
            request_type = "SessionEndedRequest"
        if "cancel".format(self.name) in words:
            request_type = "IntentRequest"
            intent_name = "AMAZON.CancelIntent"
        if "stop".format(self.name) in words:
            request_type = "IntentRequest"
            intent_name = "AMAZON.StopIntent"

        print("you asked, '{}'".format(words))

        sample_utterance = "HowsItGoing how is {subject} going"
        utterance_regex = r'how is (.*) going'
        value = re.match(utterance_regex, words)
        if value != None:
            intent_name = re.match(r'^\w+', sample_utterance).group(0)
            print("intent_name is '{}'".format(intent_name))
            value = value.group(1)
            print("value is '{}'".format(value))
            request_type = "IntentRequest"
            slots = {
                "subject": {
                    "name": "subject",
                    "value": value
                }
            }
        if "say hello" in words:
            intent_name = "IntroduceYourself"
            request_type = "IntentRequest"

        print("request_type is '{}'".format(request_type))
        print("slots is '{}'".format(slots))

        request = self.alexa(new_session, request_type, intent_name, slots)
        service_response = self.handler.hello(request, None)
        return service_response


    def timeout(self):
        new_session = self.activate()
        intent_name = None
        slots = None
        request_type = "SessionEndedRequest"
        service_request = self.alexa(new_session, request_type, intent_name, slots)
        service_request["request"]["reason"] = 'EXCEEDED_MAX_REPROMPTS'
        service_response = self.handler.hello(service_request, None)
        text = service_response["response"]["outputSpeech"]["text"]
        return text


    def alexa(self, new_session, request_type, intent_name, slots):
        # new_session = True or False
        # request_type = "LaunchRequest", "IntentRequest"
        # intent_name = "CanItEat" (from sample_utterances.txt)
        service_request = {
            "session": {
                "new": new_session,
                "sessionId": "SessionId.c1bbb5bf-29dd-430b-8476-50fd4958200c",
                "application": {
                    "applicationId": "amzn1.ask.skill.5858d1a6-2fce-4ae7-889a-d2932738db27"
                },
                "attributes": {},
                "user": {
                    "userId": "amzn1.ask.account.AEUPDEZTCS5ZATUSUS6ZNPBZ7FJ66NRFEWPWOR7LB2HHT3EPN42RTYUXNLBF62TXPVKTYWXCLZXIOI3AHNOPM4AAANBFOXRSD2PSTGBYPQ7WLJDRRHGX3LNQY5OJRO3LQRWORZNSJOPQSJKADPCBCBSVSQ2YAQRTJY2SINVK3TGCPKMRBCYHHCN7BXKTJDXS45FTXU3E74M25EI"
                }
            },
            "context": {
                'AudioPlayer': {
                    'playerActivity': 'IDLE'
                },
                'System': {
                    'application': {
                        'applicationId': 'amzn1.ask.skill.5858d1a6-2fce-4ae7-889a-d2932738db27'
                    },
                    'user': {
                        'userId': 'amzn1.ask.account.AEUPDEZTCS5ZATUSUS6ZNPBZ7FJ66NRFEWPWOR7LB2HHT3EPN42RTYUXNLBF62TXPVKTYWXCLZXIOI3AHNOPM4AAANBFOXRSD2PSTGBYPQ7WLJDRRHGX3LNQY5OJRO3LQRWORZNSJOPQSJKADPCBCBSVSQ2YAQRTJY2SINVK3TGCPKMRBCYHHCN7BXKTJDXS45FTXU3E74M25EI'
                    },
                    'device': {
                        'deviceId': 'amzn1.ask.device.AFGFPTAZDZPMLQCJDYGS2Z4QKWYFJWCTA3OHH2RNWKI2N4TORNCTCMYJO64S24TCQIBU3ODIB2432MO3VSB2EPABIHYOXKB7WAJJHDPVH7GDPRUBBEFJB3XYAA22QLT4K5EQJPCKKWW6ID3ESP4FNGYIKN4Q', 'supportedInterfaces': {
                            'AudioPlayer': {}
                        }
                    },
                    'apiEndpoint': 'https://api.eu.amazonalexa.com'
                }
            },
            "request": {
                "type": request_type,
                "requestId": "EdwRequestId.2de16d67-ca96-4417-b307-add19c9fe10d",
                "locale": "en-GB",
                "timestamp": "2017-04-28T09:29:15Z"
            },
            "version": "1.0"
        }
        if "SessionEndedRequest" in request_type:
            service_request["request"]["reason"] = 'USER_INITIATED'
            #  EXCEEDED_MAX_REPROMPTS if timed out
            self.active = False
        if "IntentRequest" in request_type:
            service_request["request"]["intent"] = {
                "name": intent_name,
                'confirmationStatus': 'NONE'
            }
        if slots != None:
            service_request["request"]["intent"]["slots"] = slots
        return service_request
