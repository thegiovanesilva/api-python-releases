from cmath import exp


class UpdateVersionRepository:
    def update_version(id, data):
        if not id:
            raise Exception('ID is required')
        if not object:
            raise Exception('Data to update is required')