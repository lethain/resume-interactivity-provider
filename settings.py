import os, datetime
from resume import *
from django.utils import simplejson
ROOT_PATH = os.path.dirname(__file__)

# setting up directory paths
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates')
)
STATIC_DIR = os.path.join(ROOT_PATH,'static')
DEPLOY_DIR = os.path.join(ROOT_PATH,'deploy')
IMAGES_DIR = os.path.join(ROOT_PATH,'images')

# setting up some helpful values
STATIC_URL_FORMAT = u"/static/%s"
STATIC_THUMBNAIL_FORMAT = STATIC_URL_FORMAT % u"thumbnail/%s"
STATIC_IMAGE_FORMAT = STATIC_URL_FORMAT % u"image/%s"
THUMBNAIL_SIZE = (128,128)

# create munged ids for experiences
import re
CHARS_TO_SUB = re.compile(r"[ .!]+")
for exp in EXPERIENCES:
    exp['id'] = CHARS_TO_SUB.subn(u"",exp['title'])[0]


# creating default rendering context
CONTEXT = {
    'name':NAME,
    'name_url':NAME_URL,
    'email':EMAIL,
    'phone':PHONE,
    'twitter':TWITTER,
    'street':STREET,
    'city':CITY,
    'zip':ZIP,
    'state':STATE,
    'country':COUNTRY,
    'statement':STATEMENT,
    'experiences':EXPERIENCES,
    'exp_json':simplejson.dumps(EXPERIENCES),
    'skills':SKILLS,
}

PAGES_TO_RENDER = (
    u"index.html",
)

INSTALLED_APPS = (
    'aym_tags',
)
