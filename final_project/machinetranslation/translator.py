import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('lI78MdwevDYKQu7oct1UK_BYZLVpWel-ibjioC0DNoOl')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    """
    This function translates English to French
    """
    frenchtranslation = language_translator.translate(
                                text=english_text,
                                model_id='en-fr'
    ).get_result()                    
    french_text = frenchtranslation.get("translations")[0].get("translation")

    return french_text


def french_to_english(french_text):
    """
    This function translates French to English
    """
    englishtranslation = language_translator.translate(
                                text=french_text,
                                model_id='fr-en'
    ).get_result()                    
    english_text = englishtranslation.get("translations")[0].get("translation")
    return english_text
