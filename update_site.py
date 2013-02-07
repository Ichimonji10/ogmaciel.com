import datetime
from jinja2 import Template, DictLoader
from jinja2.environment import Environment


BITBUCKET = 'img/bitbucket.png'
LASTFM = 'img/lastfm.png'
FACEBOOK = 'img/facebook.png'
INSTAGRAM = 'img/instagram.png'
TUMBLR = 'img/tumbrl.png'
GITHUB = 'img/github.png'
GPLUS = 'img/google_plus.png'
TWITTER = 'img/twitter.png'
FLICKR = 'img/flickr.png'
GOODREADS = 'img/goodreads.png'
LINKEDIN = 'img/linkedin.png'


sites = {'sites': {
        'bitbucket': {
            'name': 'BitBucket',
            'url': 'https://bitbucket.org/omaciel',
            'img': BITBUCKET},
        'lastfm': {
            'name': 'Last.fm',
            'url': 'http://www.last.fm/user/OgMaciel',
            'img': LASTFM},
        'facebook': {
            'name': 'Facebook',
            'url': 'https://www.facebook.com/og.maciel',
            'img': FACEBOOK},
        'instagram': {
            'name': 'Instagram',
            'url': 'http://instagram.com/ogmaciel/',
            'img': INSTAGRAM},
        'blog1': {
            'name': 'Blog: English',
            'url': 'http://ogmaciel.tumblr.com/tagged/english',
            'img': TUMBLR},
        'blog2': {
            'name': 'Blog: Portuguese',
            'url': 'http://ogmaciel.tumblr.com/tagged/portuguese',
            'img': TUMBLR},
        'github': {
            'name': 'Github',
            'url': 'https://github.com/omaciel',
            'img': GITHUB},
        'gplus': {
            'name': 'Google Plus',
            'url': 'https://plus.google.com/u/0/101951976359009287197/about',
            'img': GPLUS},
        'twitter': {
            'name': 'Twitter',
            'url': 'https://twitter.com/OgMaciel',
            'img': TWITTER},
        'flickr': {
            'name': 'Flickr',
            'url': 'http://www.flickr.com/people/ogmaciel/',
            'img': FLICKR},
        'goodreads': {
            'name': 'GoodReads',
            'url': 'http://www.goodreads.com/user/show/12048315-og-maciel',
            'img': GOODREADS},
        'linkedin': {
            'name': 'Linkedin',
            'url': 'http://www.linkedin.com/pub/og-maciel/7/425/257/',
            'img': LINKEDIN},
        }}

vars = {
    'year': datetime.datetime.today().year,
    'user': 'Og Maciel'}

vars.update(sites)

#template_name = 'base.html'
#template = Template(open(template_name).read())

#result = template.render(vars)

env = Environment()

#TODO: Move *.html files to a template dir and auto discover them.
pages = ('base.html', 'content.html')
templates = dict((name, open(name, 'rb').read()) for name in pages)
env.loader = DictLoader(templates)


env.loader = DictLoader(templates)

tmpl = env.get_template('content.html')
result = tmpl.render(vars)

print result
