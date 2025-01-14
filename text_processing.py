import re
from textblob import TextBlob
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from googletrans import Translator
from transformers import pipeline

class TextProcessor:
    def __init__(self):
        self.emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

    def clean_tweet(self, tweet):
        
        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def translate_tweet(self, tweet):
        
        translator = Translator()
        try:
            lang = detect(tweet)
            if lang != 'en':
                translated = translator.translate(tweet, src=lang, dest='en')
                return translated.text
            return tweet
        except LangDetectException:
            return tweet

    def get_sentiment(self, tweet):
        
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def classify_emotions(self, tweet):
        
        try:
            predictions = self.emotion_classifier(tweet)
            return [pred['label'] for pred in predictions if pred['score'] > 0.5]
        except Exception as e:
            print("Error in emotion classification:", e)
            return ["unknown"]
