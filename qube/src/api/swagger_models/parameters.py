from qube.src.api.swagger_models.testpythonresource \
    import TestPythonResourceModel, TestPythonResourceModelPost

"""
swagger parameters definitions
"""
header_ex = {
    "type": "string",
    "description": "Custom header that is expected as part of the request",
    "name": "Authorization",
    "in": "header",
    "required": False
}

path_ex = {
    "type": "string",
    "description": "This is the part of the URL",
    "name": "entity_id",
    "in": "path",
    "required": True
}

query_ex = {
    "type": "string",
    "description": "Query string appended to the URL",
    "name": "sth",
    "in": "query",
    "required": True
    # "required": False
}

body_ex = {
    'name': 'body',
    'description': 'Request body',
    'in': 'body',
    'schema': TestPythonResourceModel,
    'required': True,
}

body_post_ex = {
    'name': 'body',
    'description': 'Request body',
    'in': 'body',
    'schema': TestPythonResourceModelPost,
    'required': True,
}

body_put_ex = {
    'name': 'body',
    'description': 'Request body',
    'in': 'body',
    'schema': TestPythonResourceModelPost,
    'required': True,
}
