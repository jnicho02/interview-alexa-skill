import unittest
import handler
from tests.mock_alexa import MockAlexa

class TestHandler(unittest.TestCase):


    def test_launch(self):
        alexa = MockAlexa("interview", handler)
        service_response = alexa.ask("open interview")
        assert "Hello" in service_response["response"]["outputSpeech"]["text"]


    def test_timeout(self):
        alexa = MockAlexa("interview", handler)
        service_response = alexa.ask("open interview")
        service_response = alexa.timeout()
        assert "Thank you for speaking to me" in service_response["response"]["outputSpeech"]["text"]


    def test_help(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        service_response = alexa.ask("help")
        assert "Hello" in service_response["response"]["outputSpeech"]["text"]


    def test_exit(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        service_response = alexa.ask("exit")
        assert "Thank you for speaking to me" in service_response["response"]["outputSpeech"]["text"]


    def test_how_is_this_talk_going(self):
        intent = {
            "name": "HowsItGoing",
            "slots": {
                "subject": {
                  "name": "subject",
                  "value": "this talk"
                }
            }
        }
        response = handler.hows_it_going(intent)
        assert "I think you are mad" in response


    def test_can_it_eat_alcohol(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        service_response = alexa.ask("how is this talk going")
        assert "I think you are med" in service_response["response"]["outputSpeech"]["text"]
