from bottle import default_app, route
from bottle import view
import MySQLdb
from bottle import request, response, static_file
from bottle import post, get, delete
from bottle import error
from bottle import hook
import json
from beaker.middleware import SessionMiddleware
from mysite.model.exception import PermissionException
from mysite.api.proxyService import ProxyService
from mysite.api.deviceService import DeviceService
from mysite.api.virtualEntityService import VirtualEntityService
from mysite.api.propertyService import PropertyService
from mysite.api.domainService import DomainService
from mysite.api.groupService import GroupService
from mysite.api.userService import UserService
from mysite.api.services.securityService import SecurityService

REGEX_URL = "([\d\w\-]+\/)*([\d\w\-]+){1}"

db =MySQLdb.connect(
    host='iot.mysql.pythonanywhere-services.com',
    user='iot',
    passwd='ChallengerSRT8',
    db='iot$database')

db.autocommit(False)

session_options = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}


app = SessionMiddleware(default_app(), session_options)



proxyService = ProxyService(db=db)
deviceService = DeviceService(db=db)
domainService = DomainService(db=db)
entityService = VirtualEntityService(db=db)
propertyService = PropertyService(db=db)
groupService = GroupService(db=db)
userService = UserService(db=db)

top_level_domain_id = domainService.get_tld_id()

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

@hook('before_request')
def create_connection():
    pass

@hook('before_request')
def check_permission():
    securityService = SecurityService(db=db)
    try:
        securityService.check_access_permission(request)
    except PermissionException:
        request.environ['PATH_INFO'] = '/error_401'
    except ValueError:
        request.environ['PATH_INFO'] = '/error_404'
    except:
        request.environ['PATH_INFO'] = '/error_500'


@get('/')
@view('public/index')
def get_index():
    pass

@get('/login')
@view('public/login')
def get_login():
    pass

@get('/register')
@view('public/register')
def get_register():
    pass

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@error(405)
def error405(error):
    return error

#################          Static Routes          ###################################
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='/static/scripts')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/images')


@get('/<filename:re:.*\.(eot|ttf|woff|woff2|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

########################################### Resources Section  ####################3


############         PROXY     ################

@get('/api/proxy')
def proxy_get():
    try:
        data = proxyService.get(ewquest)
        return compose_response(200, data,"OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

@post('/api/proxy')
def proxy_post():
    try:
        data = request.json
        proxyService.set(data)
        return compose_response(200,data,"OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

@delete('/api/proxy')
def proxy_delete():
    try:
        data = request.json
        proxyService.delete(data)
        return compose_response(200,data,"OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

############         ENTITY     ################

@get('/api/entity')
def entity_get():
    try:
        data = entityService.get(request)
        return compose_response(200, data,"OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

@post('/api/entity')
def entity_post():
    try:
        data = entityService.set(request)
        return compose_response(200, data,"OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

@delete('/api/entity')
def entity_delete():
    try:
        data = entityService.delete(request)
        return compose_response(200, data,"OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

############         GROUP     ################

@get('/api/group')
def group_post():
    try:
        data = groupService.get(request)
        return compose_response(200, data, "OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

@post('/api/group')
def group_post():
    try:
        data = groupService.set(request)
        return compose_response(200, data, "OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

@delete('/api/group')
def group_post():
    try:
        data = groupService.delete(request)
        return compose_response(200, data, "OK")
    except Exception:
        return compose_response(500, "Internal Server Error")

####################  USER Section  ###################################

@post('/register')
def register():
    try:
        data = request.json
        userService.register(data)
        return compose_response(200, "Registration successful")
    except Exception:
        return compose_response(500, "Internal Server Error")


@post('/login')
def login():
    try:
        userService.sign_in(request)
        return compose_response(200, "Login OK")
    except Exception:
        return compose_response(500,"Internal Server Error")

@get('/logout')
def logout():
    try:
        userService.sign_out(request)
        return compose_response(200, "Logout success")
    except Exception:
        return compose_response(500, "Internal Server Error")

@get('/session')
def trySession():
    if 'something' in request.session:
        print(request.session['something'])
        return 'It worked!'

    request.session['something'] = 1

#############  RESPONSE SECTION #############################3

@route('/error_401')
def rbac_error_response():
    response.content_type = 'application/json'
    response.status = 401
    return json.dumps({'Error': "Authorisation required"})

@route('/error_404')
def resource_error_response():
    response.content_type = 'application/json'
    response.status = 404
    return json.dumps({'Error': "Resource not found"})

@route('/error_500')
def internal_error_response():
    response.content_type = 'application/json'
    response.status = 500
    return json.dumps({'Error': "Internal Server Error"})


def compose_response(code , data = None , message=""):
    response.content_type = 'application/json'
    response.status = code
    return json.dumps({'Data': data, "message" : message})

application = app



