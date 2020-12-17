# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPharmacyFacility(Action):

    def name(self) -> Text:
        return "action_pharmacy_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have a pharmacy list yet")

        return []

class ActionHealthFacility(Action):

    def name(self) -> Text:
        return "action_health_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have a health facility list yet")

        return []

class ActionCovidHealthFacility(Action):

    def name(self) -> Text:
        return "action_covid_health_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have a covid health facility list yet")

        return []

		
class ActionHospitalList(Action):

    def name(self) -> Text:
        return "action_covid_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have a hospital list yet")

        return []

		
class ActionQuarantineFacility(Action):

    def name(self) -> Text:
        return "action_covid_patient_quarantine_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have a quaratine area list yet")

        return []

		
class ActionCasesStat(Action):

    def name(self) -> Text:
        return "action_covid_cases_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have cases statitistics yet")

        return []

		
class ActionConfineStats(Action):

    def name(self) -> Text:
        return "action_confinment_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I don't have confinment statitistics yet")

        return []
