import sys
reload(sys)
sys.path.append('./plugins/')
sys.setdefaultencoding('utf-8')

import bayes
import controller
import os
import sae
import web
import jieba

web.config.debug = True  
        
urls = (
    '/', 'Index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

class Index:        
    def GET(self):
        return render.index()
    def POST(self):
        data = web.input()
        words = data.queryword;
        words_cut = controller.CutWords(words)
        combine = controller.GetCategories(words_cut)
        #combine = bayes.GetCategories(words_cut)
        return render.queryword(combine)

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)