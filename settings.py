import os, datetime
from django.utils import simplejson
ROOT_PATH = os.path.dirname(__file__)

EXPERIENCES = (
    {
        "title":"Irrational Exuberance",
        "link":"http://lethain.com/",
        "start":"May, 2007",
        "end":"Present",
        "skills":("Django","Python","JavaScript","Cocoa","PyObjC","Cappuccino","Processing.js","Yahoo! BOSS",),
        "description":"Write about Django, Python and programming topics.",
        },
    {
        "title":"Touch Defense",
        "link":"http://touchdefense.com/",
        "start":"July, 2008",
        "end":"Present",
        "description":"Not yet released project with <a href='http://lukehatcher.com'>Luke Hatcher</a>.",
        "skills":("Objective-C","Cocoa","iPhone"),
        },
    {
        "title":"AYM CMS",
        "link":"http://aymcms.com/",
        "start":"September, 2008",
        "end":"",
        "description":"Create static websites using Django's flexibility.",
        "skills":("Python","Django","HTML","CSS"),
        },
    {
        "title":"Sparklines.js",
        "link":"http://www.willarson.com/code/sparklines/sparklines.html",
        "start":"June, 2008",
        "description":"Library for creating statistically sound sparklines.",
        "skills":("JavaScript","Processing.js"),
        },
    {
        "title":"LifeFlow",
        "link":"http://lethain.com/",
        "start":"August, 2007",
        "end":"Present",
        "description":"Feature-rich blogging application in Django.",
        "skills":("Django","Python","HTML","CSS","JavaScript","jQuery"),
        },
    {
        "title":"JET Program",
        "link":"http://www.jetprogramme.org/",
        "start":"August, 2007",
        "end":"August, 2008",
        "description":"Taught English in three public schools in Japan.",
        "skills":("Japanese",),
        },
    {
        "title":"Processed Tower Defense",
        "link":"http://ptdef.com/about.html",
        "start":"May, 2008",
        "end":"June, 2008",
        "description":"Created tower defense game with <a href='http://blog.rictic.com/'>Peter Burns</a>.",
        "skills":("JavaScript","Processing.js","jQuery","HTML","CSS"),
        },
    {
        "title":"Centre College",
        "link":"http://centre.edu/",
        "start":"August, 1999",
        "end":"May, 2003",
        "description":"B.S. of Computer Science. Member of Phi Beta Kappa.",
        "skills":("Java","Subversion","Python","Japanese"),
        },
)

"""
    {
        "title":"",
        "link":"http://",
        "start":"",
        "end":"",
        },
"""

SKILLS = (
    'Python',
    'JavaScript',
    'Objective-C',
    'Java',
    'PHP',
    'Common Lisp',
    'Django',
    'Cocoa',
    'PyObjC',
    'iPhone',
    'jQuery',
    'YUI',
    'Cappuccino',
    'Processing.js',
    'Yahoo! BOSS',
    'Google App Engine',
    'PostgreSQL',
    'SQLite',
    'Memcached',
    'HTML',
    'CSS',
    'Git',
    'Mercurial',
    'Subversion',
    'Japanese',
)

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

NAME = u"Will Larson"
NAME_URL = u"http://lethain.com/"
EMAIL = u"lethain@gmail.com"
PHONE = u"(828) 275-9714"
TWITTER = u"Lethain"
STREET = u"265 Linden Ave."
CITY = "Verona"
ZIP = "07044"
STATE = "NJ"
COUNTRY = "USA"

STATEMENT = """
I am a contract programmer. I do web development with Django,
Python, PHP, JavaScript, HTML and CSS. I implement Apple software
(OSX and iPhone) with Objective-C, Cocoa and PyObjC. I like to
write tutorials, and about new libraries.

I've stopped using the Oxford comma.

"""

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
