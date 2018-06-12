from adapters.exceptions import NoRecordFound
from pg import DB, DatabaseError


def _normalize(record):
    inhabitant = record["data"]
    inhabitant["Id"] = str(record["id"])
    return inhabitant


class PostgresqlAdapter(object):

    def __init__(self, dbname, user, passwd, host="localhost", port=5432):
        self._db = DB(dbname=dbname, host=host, port=port, user=user, passwd=passwd)

    def create(self, inhabitant):
        record = self._db.insert('inhabitants', data=inhabitant)
        return _normalize(record)

    def find_all(self):
        all_inhabitants = self._db.query('select * from inhabitants').dictresult()
        return [_normalize(x) for x in all_inhabitants]

    def find_by_id(self, id):
        inhabitant = self._find_by_id(id)
        return _normalize(inhabitant)

    def find_by_name(self, name):
        all_inhabitants = self._db.query(
            "SELECT * FROM inhabitants " +
            "WHERE data ->> 'FirstName' ILIKE '%' || $1 || '%' OR " +
            "      data ->> 'LastName' ILIKE '%' || $1 || '%'", (name,)
        ).dictresult()
        return [_normalize(x) for x in all_inhabitants]

    def delete(self, id):
        try:
            self._db.delete('inhabitants', id=int(id))
        except ValueError:
            pass

    def update(self, inhabitant):
        id = inhabitant["Id"]
        self._find_by_id(id)
        del inhabitant["Id"]
        stored = self._db.update('inhabitants', id=id, data=inhabitant)
        return _normalize(stored)

    def _find_by_id(self, id):
        try:
            return self._db.get('inhabitants', int(id))
        except (ValueError, DatabaseError):
            raise NoRecordFound()
