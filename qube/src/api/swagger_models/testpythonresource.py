from flask_restful_swagger_2 import Schema


class VersionModel(Schema):
    type = 'object'
    properties = {
        'version': {
            'type': 'string',
        }
    }


class TestPythonResourceModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'string',
        },
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'tenantId': {
            'type': 'string'
        },
        'orgId': {
            'type': 'string'
        },
        'createdBy': {
            'type': 'string'
        },
        'createdDate': {
            'type': 'string'
        },
        'modifiedBy': {
            'type': 'string'
        },
        'modifiedDate': {
            'type': 'string'
        }
    }
    required = ['name']


class TestPythonResourceModelPost(Schema):
    type = 'object'
    properties = {
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        }
    }
    required = ['name']


class TestPythonResourceModelPut(Schema):
    type = 'object'
    properties = {
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        }
    }


class TestPythonResourceModelPostResponse(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'string'
        }
    }


class TestPythonResourceErrorModel(Schema):
    type = 'object'
    properties = {
        'error_code': {
            'type': 'string'
        },
        'error_message': {
            'type': 'string'
        }
    }
    required = ['name']
