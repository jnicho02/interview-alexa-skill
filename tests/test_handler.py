import unittest
import handler
from tests.mock_alexa import MockAlexa

class TestHandler(unittest.TestCase):


    def test_launch(self):
        alexa = MockAlexa("interview", handler)
        alexa_says = alexa.ask_text("open interview")
        assert "Hello" in alexa_says


    def test_timeout(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        alexa_says = alexa.timeout()
        assert "Thank you for speaking to me" in alexa_says


    def test_help(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        alexa_says = alexa.ask_text("help")
        assert "Hello" in alexa_says


    def test_exit(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        alexa_says = alexa.ask_text("exit")
        assert "Thank you for speaking to me" in alexa_says


    def test_introduction_intent(self):
        intent = {
            "name": "IntroduceYourself"
        }
        alexa_says = handler.introduce_yourself(intent)
        assert "my name is Alexa" in alexa_says


    def test_introduction_intent(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        alexa_says = alexa.ask_text("say hello")
        assert "my name is Alexa" in alexa_says


    def test_say_how_is_this_talk_going(self):
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
        assert "I think you are mad" in response \
        or "Did you think this through" in response \
        or "I wish you good luck" in response \
        or "I am here to help" in response


    def test_how_is_this_talk_going(self):
        alexa = MockAlexa("interview", handler)
        alexa.ask("open interview")
        alexa_says = alexa.ask_text("how is this talk going")
        assert "I think you are mad" in alexa_says \
        or "Did you think this through" in alexa_says \
        or "I wish you good luck" in alexa_says \
        or "I am here to help" in alexa_says
