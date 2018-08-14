
import re
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.util.log import getLogger
from adapt.intent import IntentBuilder

import json
import requests


LOGGER = getLogger(__name__)


class Juniper_skill(MycroftSkill):
    def __init__(self):
        super(Juniper_skill, self).__init__(name="Juniper_skill")

    @intent_handler(IntentBuilder("Good_device").require("Query").require("Juniper").require("input_id"))
    def handle_intent(self, message):
        # Extract what the user asked about
        device_id = message.data.get("input_id")
        #str1 = "good device"
        output = self.call_api_output(device_id)


        self.speak_dialog("Good",{"status":output})

    def call_api_output(self,device_id):
        todo_id = device_id
        data  = requests.get("http://127.0.0.1:5000/todos/"+todo_id)
        json_data = data.json()
        output = json_data['task']
        return output







def create_skill():
    return Juniper_skill()
