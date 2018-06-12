import uuid
import re

from adapters.exceptions import NoRecordFound


class MemoryAdapter(object):
    _inhabitants = {}

    def create(self, inhabitant):
        id = str(uuid.uuid1())
        inhabitant["Id"] = id
        self._inhabitants[id] = inhabitant
        return inhabitant

    def find_all(self):
        return list(self._inhabitants.values())

    def find_by_id(self, id):
        self._ensure_exists(id)
        return self._inhabitants[id]

    def find_by_name(self, name):
        pattern = re.compile("(?i).*" + re.escape(name))

        def matches_name(x):
            return pattern.match(x["FirstName"]) is not None or \
                   pattern.match(x["LastName"]) is not None

        return [x for x in self._inhabitants.values() if matches_name(x)]

    def delete(self, id):
        if self._inhabitants[id] is not None:
            del self._inhabitants[id]

    def update(self, inhabitant):
        id = inhabitant["Id"]
        self._ensure_exists(id)
        self._inhabitants[id] = inhabitant
        return inhabitant

    def _ensure_exists(self, id):
        if not id in self._inhabitants:
            raise NoRecordFound()
