from bson import ObjectId
from bson.errors import InvalidId
from adapters.exceptions import NoRecordFound
from pymongo import MongoClient
import re


def _normalize(inhabitant):
    inhabitant["Id"] = str(inhabitant["_id"])
    del inhabitant["_id"]
    return inhabitant


class MongoDbAdapter(object):

    def __init__(self, connection_string):
        self._client = MongoClient(connection_string)
        self._db = self._client.UNHCR
        self._inhabitants = self._db.Inhabitants

    def create(self, inhabitant):
        self._inhabitants.insert_one(inhabitant)
        return _normalize(inhabitant)

    def find_all(self):
        all_inhabitants = self._inhabitants.find()
        return [_normalize(x) for x in all_inhabitants]

    def find_by_id(self, id):
        inhabitant = self._find_by_id(id)
        return _normalize(inhabitant)

    def find_by_name(self, name):
        pattern = "(?i).*" + re.escape(name)
        all_inhabitants = self._inhabitants.find({"$or": [
            {"FirstName": {"$regex": pattern}},
            {"LastName": {"$regex": pattern}}
        ]})
        return [_normalize(x) for x in all_inhabitants]

    def delete(self, id):
        try:
            object_id = ObjectId(id)
            self._inhabitants.delete_one({"_id": object_id})
        except InvalidId:
            pass

    def update(self, inhabitant):
        id = inhabitant["Id"]
        stored = self._find_by_id(id)
        inhabitant["_id"] = stored["_id"]
        self._inhabitants.save(inhabitant)
        return _normalize(inhabitant)

    def _find_by_id(self, id):
        try:
            object_id = ObjectId(id)
        except InvalidId:
            raise NoRecordFound()
        inhabitant = self._inhabitants.find_one(object_id)
        if inhabitant is None:
            raise NoRecordFound()
        return inhabitant

    def _ensure_exists(self, id):
        raise Exception
