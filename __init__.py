from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.util.log import getLogger
from adapt.intent import IntentBuilder


LOGGER = getLogger(__name__)


class Juniper_skill(MycroftSkill):
    def __init__(self):
        super(Juniper_skill, self).__init__(name="Juniper_skill")

    @intent_handler(IntentBuilder("Good_device").require("Query").require("Juniper"))
    def handle_intent(self, message):
        # Extract what the user asked about
        self.speak_dialog("Good")



def create_skill():
    return Juniper_skill()
