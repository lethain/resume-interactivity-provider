import os, datetime
from django.utils import simplejson
ROOT_PATH = os.path.dirname(__file__)

EXPERIENCES = (
    {
        "title":"Irrational Exuberance",
        "link":"http://lethain.com/",
        "start":"May, 2007",
        "end":"Present",
        "skills":("Writing",),
        "description":"I write about Django, Python and many other things.",
        },
    {
        "title":"Sparklines.js",
        "link":"http://lethain.com/",
        "start":"June 2008",
        "end":"Present",
        "description":"A JavaScript library for creating statistically sound cross-browser sparklines.",
        "skills":("JavaScript","Processing.js"),
        },
    {
        "title":"LifeFlow",
        "link":"http://lethain.com/",
        "start":"",
        "end":"",
        "skills":("Django","Python","HTML","CSS","JavaScript","jQuery","PostgreSQL","Memcached","Git"),
        },
    {
        "title":"Japanese Exchange and Teaching Program",
        "link":"http://lethain.com/",
        "start":"",
        "end":"",
        "skills":("Japanese","Teaching",),
        },
    {
        "title":"Centre College",
        "link":"http://lethain.com/",
        "start":"",
        "end":"",
        "skills":("Java",),
        },
    {
        "title":"Processed Tower Defense",
        "link":"http://lethain.com/",
        "start":"",
        "end":"",
        "skills":("JavaScript","Processing.js","HTML","CSS"),
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
    'PostgreSQL',
    'SQLite',
    'Memcached',
    'HTML',
    'CSS',
    'Git',
    'Mercurial',
    'Subversion',
    'Japanese',
    'Teaching',
    'Writing',
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
I am the contract programmer who will solve your problem.
I won't disappear into another dimension while working; I'll
keep you informed. I won't conduct maniacal experiments with
your project; I'll build it with appropriate tools, adhering
to relevant standards.

I do web development with Django, Python, PHP, JavaScript, HTML
and CSS. I develop Apple software (OSX and iPhone) with Objective-C,
Cocoa and PyObjC.

"""

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
