'''
ibm python dev assignment using ibm watson translation service
'''
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    EN to FR
    '''
    if english_text:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        #translation_json=json.dumps(translation, indent=2, ensure_ascii=False)
        return translation["translations"][0]["translation"]

    return "empty"

def french_to_english(french_text):
    '''
    FR to EN
    '''
    if french_text:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        #translation_json=json.dumps(translation, indent=2, ensure_ascii=False)
        return translation["translations"][0]["translation"]

    return "empty"
