from bottle import default_app, route, redirect
from bottle import view
from bottle import request, response, static_file
from bottle import post, get, delete, put
from bottle import error
from bottle import hook
import json
import logging
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

session_options = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}



app = SessionMiddleware(default_app(), session_options)

userService = UserService()


@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

@hook('before_request')
def check_permission():
    if request.path.startswith('/error'):
        return
    securityService = SecurityService()
    try:
        securityService.check_access_permission(request)
    except PermissionException:
        redirect('/error/api/401')
    except ValueError:
        redirect('/error/api/404')
    except:
        logging.exception("Something awful happened!")
        redirect('/error/api/500')

@get('/')
@view('public/index')
def get_index():
    user = userService.get_user(request)
    return dict(user=user)

@get('/login')
@view('public/login')
def get_login():
    pass

@get('/register')
@view('public/register')
def get_register():
    pass

@get('/admin')
@view('admin/index')
def admin_index():
    try:
        user = userService.get_user(request)
        return dict(user=user)
    except:
        request.environ['PATH_INFO'] = '/error_404'

@get('/admin/entity')
@view('admin/entity')
def load_admin_entity_page():
    try:
        user = userService.get_user(request)
        return dict(user=user)
    except:
        request.environ['PATH_INFO'] = '/error_404'

@get('/admin/proxy')
@view('admin/proxy')
def load_admin_proxy_page():
    try:
        user = userService.get_user(request)
        return dict(user=user)
    except:
        request.environ['PATH_INFO'] = '/error_404'

@get('/admin/domain')
@view('admin/domain')
def load_admin_domain_page():
    try:
        user = userService.get_user(request)
        return dict(user=user)
    except:
        request.environ['PATH_INFO'] = '/error_404'



@error(404)
@view('public/page404')
def error404(error):
    try:
        user = userService.get_user(request)
        return dict(user=user)
    except:
        return dict(user=None)

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
        proxyService = ProxyService()
        data = proxyService.get(request)
        return compose_response(200, data,"OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

@post('/api/proxy')
def proxy_post():
    try:
        proxyService = ProxyService()
        data = request.json
        proxyService.set(data)
        return compose_response(200,data,"OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

@put('/api/proxy')
def proxy_put():
    try:
        proxyService = ProxyService()
        data = request.json
        proxyService.put(data)
        return compose_response(200,data,"OK")
    except Exception as e:
        logging.exception("Something awful happened!")
        return compose_response(500,str(e), "Internal Server Error")


@delete('/api/proxy/<id>')
def proxy_delete(id):
    try:
        proxyService = ProxyService()
        data = request.json
        proxyService.delete(id)
        return compose_response(200,data,"OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

############         ENTITY     ################

@get('/api/entity/<url:path>')
def entity_get(url):
    try:
        entityService = VirtualEntityService()
        data = entityService.get(url)
        return compose_response(200, data,"OK")
    except Exception as e:
        logging.exception("Something awful happened!")
        return compose_response(500,str(e), "Internal Server Error")

@get('/api/entity')
def entity_get_all():
    try:
        entityService = VirtualEntityService()
        data = entityService.get("")
        return compose_response(200, data,"OK")
    except Exception as e:
        logging.exception("Something awful happened!")
        return compose_response(500,str(e), "Internal Server Error")

@post('/api/entity')
def entity_post():
    try:
        entityService = VirtualEntityService()
        data = entityService.set(request)
        return compose_response(200, data,"OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

@delete('/api/entity/<id>')
def entity_delete(id):
    try:
        entityService = VirtualEntityService()
        data = entityService.delete(id)
        return compose_response(200, data,"OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")
############         DOMAIN     ###############

@get('/api/domain')
@get('/api/domain/<id>')
def domain_get(id = None):
    try:
        domainService = DomainService()
        data = domainService.get(id)
        return compose_response(200, data,"OK")
    except Exception as e:
        logging.exception("Something awful happened!")
        return compose_response(500,str(e), "Internal Server Error")

@post('/api/domain')
def domain_post():
    try:
        domainService = DomainService()
        data = domainService.set(request.json)
        return compose_response(200, data,"OK")
    except Exception as e:
        logging.exception("Something awful happened!")
        return compose_response(500,str(e), "Internal Server Error")

############         GROUP     ################

@get('/api/group')
def group_get():
    try:
        groupService = GroupService()
        data = groupService.get(request)
        return compose_response(200, data, "OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

@post('/api/group')
def group_post():
    try:
        groupService = GroupService()
        data = groupService.set(request)
        return compose_response(200, data, "OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

@delete('/api/group')
def group_delete():
    try:
        groupService = GroupService()
        data = groupService.delete(request)
        return compose_response(200, data, "OK")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

####################  USER Section  ###################################

@post('/register')
def register():
    try:
        userService = UserService()
        data = request.json
        userService.register(data)
        return compose_response(200, "Registration successful")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")


@post('/login')
def login():
    try:
        userService = UserService()
        userService.sign_in(request)
        return compose_response(200, "Login OK")
    except Exception as e:
        return compose_response(500,str(e),"Internal Server Error")

@get('/logout')
def logout():
    try:
        userService = UserService()
        userService.sign_out(request)
        return compose_response(200, "Logout success")
    except Exception as e:
        return compose_response(500,str(e), "Internal Server Error")

@get('/session')
def trySession():
    if 'something' in request.session:
        print(request.session['something'])
        return 'It worked!'

    request.session['something'] = 1

#############  RESPONSE SECTION #############################3

@route('/error/api/401')
def rbac_error_response():
    response.content_type = 'application/json'
    response.status = 401
    return json.dumps({'Error': "Authorisation required"})

@route('/error/api/404')
def resource_error_response():
    response.content_type = 'application/json'
    response.status = 404
    return json.dumps({'Error': "Resource not found"})

@route('/error/api/500')
def internal_error_response():
    response.content_type = 'application/json'
    response.status = 500
    return json.dumps({'Error': "Internal Server Error"})


def compose_response(code , data = "" , message=""):
    response.content_type = 'application/json'
    response.status = code
    return json.dumps({'result': data, "message" : message})

application = app



