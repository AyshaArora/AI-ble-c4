# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideLegalAid(Action):
    def name(self):
        return "action_provide_legal_aid"

    def run(self, dispatcher, tracker, domain):
        response = ("Here are some confidential legal resources:\n"
                    "- [Ontario Justice Education Network](https://ojen.ca)\n"
                    "- Legal Aid Ontario: 1-800-668-8258\n"
                    "- [Canadian Centre for Refugee & Immigrant Health](https://ccrweb.ca)")
        dispatcher.utter_message(text=response)
        return []

