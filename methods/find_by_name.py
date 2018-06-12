import methods
import adapters


def execute(adapter, id):
    try:
        return adapter.find_by_name(id)
    except adapters.NoRecordFound:
        raise methods.NoRecordFound()
