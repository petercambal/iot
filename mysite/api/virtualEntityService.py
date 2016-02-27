#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.adapters.virtualEntityAdapter import VirtualEntityAdapter

class VirtualEntityService:

    db = None
    cursor = None

    def __init__(self,db):
        self.db = db
        self.cursor = self.db.cursor()

    def get(self):
        entityAdapter = VirtualEntityAdapter(self.cursor)
        entities = entityAdapter.getAll()

        result = []
        for entity in entities:
            result.append(entity.toJSON())
        return result

    def set(self):
       pass

    def delete(self):
       pass


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



