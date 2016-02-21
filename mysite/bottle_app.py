
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route
from bottle import view
import MySQLdb
from bottle import request, response
from bottle import post, get, delete
from bottle import error
from bottle import hook
import json
import traceback
from beaker.middleware import SessionMiddleware

from mysite.model.exception import PermissionException
from mysite.api.proxyService import ProxyService
from mysite.api.deviceService import DeviceService
from mysite.api.virtualEntityService import VirtualEntityService
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
# propertyService = PropertyService(db=db)
groupService = GroupService(db=db)
userService = UserService(db=db)

top_level_domain_id = domainService.get_tld_id()
response.content_type = 'application/json'

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
    except PermissionException as e:
        return json.dumps({'Error': str(e)})



@hook('after_request')
def close_connection():
    pass
@route('/')
@view('public/index')
def hello_world():
    pass

# @get('/login')
# @view('public/login')
# def get_login():
#     pass

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@error(405)
def error405(error):
    return error

# @get('/api/proxies/<id:re:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}>')
# @get('/api/proxies') #, apply=[check_permission()]
# def proxy_id_handler(id=None):
#     proxies = proxyService.getProxy(id)
#     if not proxies:
#         return json.dumps({'Error': 'Proxy not found'})
#     return json.dumps({'Data': proxies})

@post('/api/proxy')
def proxy_post():
    try:
        data = request.json
        proxyService.set(data)
        return json.dumps({'Data': data})
    except Exception as e:
        return json.dumps({'Error': str(e)})
    # if data == None:
    #     return json.dumps({'Code':"1",'Message':'No data sent!'})
    # else:
    #     data['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
    #     # register proxy
    #     proxyService.insertOrUpdate(data)
    #     #register devices
    #     for device in data['devices']:
    #         deviceService.insertDevice(device)

    #     #register virtualEntity
    #     entityService.createVirtualEntity(data);
    #     # register properties

    #     return json.dumps({'Code':"0","Devices":data['devices']})

@delete('/api/proxy')
def proxy_delete():
    data = request.json
    proxyService.delete(data)
    return json.dumps({'Data': data})

@post('/api/group')
def group_post():
    response = groupService.post()
    return json.dumps({"Response" : response})

# @get('/api/entity/<id:re:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}>')
# @get('/api/entity')
# def getEntityHandler(id=None):
#     entities = entityService.getVirtualEntity(id)
#     if not entities:
#         return json.dumps({'Error': 'Virtual entity not found'})
#     return json.dumps({'Data': entities})

# @get('/api/entity/<url:path>')
# def proxy_path_handler(url):
#     path = re.match(REGEX_URL, url).group()
#     if not path is url:
#         error405('wrong url')
#     domains = path.split('/')
#     parent_id = top_level_domain_id
#     name = domains.pop()
#     for domain in domains:
#         domain_id = domainService.find_domain(domain,parent_id)
#         parent_id = domain_id

#     entity = entityService.get_virtual_entity(domain_id,name)

#     return json.dumps({'Data': entity})

@get('/api/entity')
def entity_get():
    response = entityService.get()
    return json.dumps({"Response" : response})

@get('/api/proxy')
def proxy_get():
    response = proxyService.get()
    return json.dumps({"Response" : response})

@post('/register')
def register():
    try:
        data = request.json
        userService.register(data)
        return json.dumps({"Response" : "OK"})
    except Exception as e:
        return json.dumps({'Error': str(e)})

@post('/login')
def login():
    try:
        userService.sign_in(request)
        return json.dumps({"Response" : "OK"})
    except Exception as e:
        return json.dumps({'Error': str(e)})

@get('/logout')
def logout():
    try:
        userService.sign_out(request)
        return json.dumps({"Response" : "Logout success"})
    except Exception as e:
        return json.dumps({'Error': str(e)})

@get('/session')
def trySession():
    if 'something' in request.session:
        print(request.session['something'])
        return 'It worked!'

    request.session['something'] = 1

application = app
