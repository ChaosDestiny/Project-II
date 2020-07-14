# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUttered, ActionExecuted
import webbrowser
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import re

class ActionCheckName(Action):

    def name(self) -> Text:
        return "action_check_name"

    @staticmethod
    def start_story_events(story_intent):
        # type: (Text) -> List[Dict]
        return [ActionExecuted("action_listen")] + [UserUttered("/" + story_intent, {
            "intent": {"name": story_intent, "confidence": 1.0},
            "entities": {}
        })]
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        if (name == None):           
            return self.start_story_events('get_name')
        else:
            return []

class ActionPlayMusic(Action):
    
    def name(self) -> Text:
        return "action_play_music"
    
    def run(self, dispatcher, tracker, domain):
        
        song = tracker.get_slot('song')
        if (song != None):
            query = urllib.parse.quote(song)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            results = re.findall(re.compile("\"/watch\?v=(.{11})"), response.read().decode())
            vid = "http://www.youtube.com/watch?v=" + results[0]
            webbrowser.open_new_tab(vid)
            return dispatcher.utter_message(text="Của bạn đây: " + vid)
        else:
            dispatcher.utter_message(text="Bạn muốn nghe bài gì?")
            return [ActionExecuted("action_listen")]
    
class ActionTellStory(Action):
    def name(self) -> Text:
        return "action_tell_story"
    
    def run(self, dispatcher, tracker, domain):
        
        story = tracker.get_slot('story')
        if (story != None):
            query = urllib.parse.quote(story)
            url = "https://truyencotich.vn/index.php?s=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            tale = soup.find_all("a", limit=16)[13]
            url = tale['href']
            if (url.find('video') == -1):
                webbrowser.open_new_tab(url)
                return dispatcher.utter_message(text="Của bạn đây: " + url)
            else:
                tale = soup.find_all("a", limit=16)[14]
                url = tale['href']   
            webbrowser.open_new_tab(url)
            return dispatcher.utter_message(text="Của bạn đây: " + url)
        else:
            dispatcher.utter_message(text="Bạn muốn tôi kể câu chuyện gì?")
            return [ActionExecuted("action_listen")]

class ActionReadPoem(Action):
    def name(self) -> Text:
        return "action_read_poem"
    
    def run(self, dispatcher, tracker, domain):
        
        poem = tracker.get_slot('poem')
        if (poem != None):
            query = urllib.parse.quote(poem)
            url = "https://poem.tkaraoke.com/tim.tho?q=" + query + "&t=2"
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            web = soup.find_all(attrs={'class':'a-name-poem'})
            if (len(web) == 0):
                webbrowser.open_new_tab(url)
                return dispatcher.utter_message(text="Của bạn đây: " + url)
            else:
                url = "https://poem.tkaraoke.com" + web[0]['href']
                webbrowser.open_new_tab(url)
                return dispatcher.utter_message(text="Của bạn đây: " + url)
        else:
            dispatcher.utter_message(text="Bạn muốn tôi đọc bài thơ gì?")
            return [ActionExecuted("action_listen")]
        
class ActionYourName(Action):

    def name(self) -> Text:
        return "action_your_name"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        if (name == None):           
            return dispatcher.utter_message(text="Xin lỗi, tôi vẫn chưa biết tên của bạn.")
        else:
            return dispatcher.utter_message(text="Bạn là " + name)