
import re
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.util.log import getLogger
from adapt.intent import IntentBuilder


LOGGER = getLogger(__name__)


class Juniper_skill(MycroftSkill):
    def __init__(self):
        super(Juniper_skill, self).__init__(name="Juniper_skill")

    @intent_handler(IntentBuilder("Good_device").require("Query").require("Juniper").require("input_id"))
    def handle_intent(self, message):
        # Extract what the user asked about
        #str1 = message.data.get("Input")
        str1 = "good device"


        self.speak_dialog("good",{"status":str1})

    #def call_api_output(self,input):




def create_skill():
    return Juniper_skill()
