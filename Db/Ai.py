from dotenv import find_dotenv, load_dotenv
from os import environ as env

import google.generativeai as genai

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

genai.configure(api_key=env.get("GEMINI_KEY"))

model = genai.GenerativeModel('gemini-pro')

def getKeywords(data):
    resp = model.generate_content(data+" give a list of keywords from the post which can be used as tags. give the keywords separated by a comma")
    return resp.text.split(',')

def getsimilarCompanies(data):
    resp = model.generate_content(data+"give a list of all comapnies from the list which are broadly similar to Wipro mention the words separated by commas, don't sayanything else")
    return resp.text.split(',')

def getsimilarTags(data):
    resp = model.generate_content(data+"give a list of all words from the list which are broadly similar to joy mention the words separated by commas, don't sayanything else")
    return resp.text.split(',')
