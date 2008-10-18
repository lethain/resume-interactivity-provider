import os, datetime
ROOT_PATH = os.path.dirname(__file__)

EXPERIENCES = (
    {
        'title':'Sparklines.js',
        'link':'http://',
        'start':'',
        'end':'',
        'skills':('JavaScript','Processing.js'),
        },
    {
        'title':'LifeFlow',
        'link':'http://',
        'start':'',
        'end':'',
        'skills':('Django','Python','HTML','CSS','JavaScript','jQuery','PostgreSQL','Memcached','Git'),
        },
    {
        'title':'Japanese Exchange and Teaching Program',
        'link':'http://',
        'start':'',
        'end':'',
        'skills':('Japanese','Teaching',),
        },
    {
        'title':'Centre College',
        'link':'http://',
        'start':'',
        'end':'',
        'skills':('Java',),
        },
    {
        'title':'Irrational Exuberance',
        'link':'http://',
        'start':'',
        'end':'',
        'skills':('Writing',),
        },
    {
        'title':'Processed Tower Defense',
        'link':'http://',
        'start':'',
        'end':'',
        'skills':('JavaScript','Processing.js','HTML','CSS'),
        },
)

"""
    {
        'title':'',
        'link':'http://',
        'start':'',
        'end':'',
        },
"""

SKILLS = (
    'Python',
    'JavaScript',
    'Objective-C',
    'Java',
    'PHP',
    'Common Lisp',
    'Django'
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
EMAIL = u"lethain@gmail.com"
PHONE = u"(828) 275-9714"
STREET = u"265 Linden Ave."
CITY = "Verona"
ZIP = "07044"
STATE = "NJ"
COUNTRY = "USA"

# creating default rendering context
CONTEXT = {
    'name':NAME,
    'email':EMAIL,
    'phone':PHONE,
    'street':STREET,
    'city':CITY,
    'zip':ZIP,
    'state':STATE,
    'country':COUNTRY,
    'experiences':EXPERIENCES,
    'skills':SKILLS,
}

PAGES_TO_RENDER = (
    u"index.html",
)

INSTALLED_APPS = (
    'aym_tags',
)
