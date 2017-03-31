#!/usr/bin/python
"""
Add docstring here
"""
import os
import time
import unittest

import mock
from mock import patch
import mongomock


with patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient):
    os.environ['TESTPYTHONRESOURCE_MONGOALCHEMY_CONNECTION_STRING'] = ''
    os.environ['TESTPYTHONRESOURCE_MONGOALCHEMY_SERVER'] = ''
    os.environ['TESTPYTHONRESOURCE_MONGOALCHEMY_PORT'] = ''
    os.environ['TESTPYTHONRESOURCE_MONGOALCHEMY_DATABASE'] = ''

    from qube.src.models.testpythonresource import TestPythonResource
    from qube.src.services.testpythonresourceservice import TestPythonResourceService
    from qube.src.commons.context import AuthContext
    from qube.src.commons.error import ErrorCodes, TestPythonResourceServiceError


class TestTestPythonResourceService(unittest.TestCase):
    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def setUp(self):
        context = AuthContext("23432523452345", "tenantname",
                              "987656789765670", "orgname", "1009009009988",
                              "username", False)
        self.testpythonresourceService = TestPythonResourceService(context)
        self.testpythonresource_api_model = self.createTestModelData()
        self.testpythonresource_data = self.setupDatabaseRecords(self.testpythonresource_api_model)
        self.testpythonresource_someoneelses = \
            self.setupDatabaseRecords(self.testpythonresource_api_model)
        self.testpythonresource_someoneelses.tenantId = "123432523452345"
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            self.testpythonresource_someoneelses.save()
        self.testpythonresource_api_model_put_description \
            = self.createTestModelDataDescription()
        self.test_data_collection = [self.testpythonresource_data]

    def tearDown(self):
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            for item in self.test_data_collection:
                item.remove()
            self.testpythonresource_data.remove()

    def createTestModelData(self):
        return {'name': 'test123123124'}

    def createTestModelDataDescription(self):
        return {'description': 'test123123124'}

    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def setupDatabaseRecords(self, testpythonresource_api_model):
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            testpythonresource_data = TestPythonResource(name='test_record')
            for key in testpythonresource_api_model:
                testpythonresource_data.__setattr__(key, testpythonresource_api_model[key])

            testpythonresource_data.description = 'my short description'
            testpythonresource_data.tenantId = "23432523452345"
            testpythonresource_data.orgId = "987656789765670"
            testpythonresource_data.createdBy = "1009009009988"
            testpythonresource_data.modifiedBy = "1009009009988"
            testpythonresource_data.createDate = str(int(time.time()))
            testpythonresource_data.modifiedDate = str(int(time.time()))
            testpythonresource_data.save()
            return testpythonresource_data

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_post_testpythonresource(self, *args, **kwargs):
        result = self.testpythonresourceService.save(self.testpythonresource_api_model)
        self.assertTrue(result['id'] is not None)
        self.assertTrue(result['name'] == self.testpythonresource_api_model['name'])
        TestPythonResource.query.get(result['id']).remove()

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_put_testpythonresource(self, *args, **kwargs):
        self.testpythonresource_api_model['name'] = 'modified for put'
        id_to_find = str(self.testpythonresource_data.mongo_id)
        result = self.testpythonresourceService.update(
            self.testpythonresource_api_model, id_to_find)
        self.assertTrue(result['id'] == str(id_to_find))
        self.assertTrue(result['name'] == self.testpythonresource_api_model['name'])

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_put_testpythonresource_description(self, *args, **kwargs):
        self.testpythonresource_api_model_put_description['description'] =\
            'modified for put'
        id_to_find = str(self.testpythonresource_data.mongo_id)
        result = self.testpythonresourceService.update(
            self.testpythonresource_api_model_put_description, id_to_find)
        self.assertTrue(result['id'] == str(id_to_find))
        self.assertTrue(result['description'] ==
                        self.testpythonresource_api_model_put_description['description'])

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_get_testpythonresource_item(self, *args, **kwargs):
        id_to_find = str(self.testpythonresource_data.mongo_id)
        result = self.testpythonresourceService.find_by_id(id_to_find)
        self.assertTrue(result['id'] == str(id_to_find))

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_get_testpythonresource_item_invalid(self, *args, **kwargs):
        id_to_find = '123notexist'
        with self.assertRaises(TestPythonResourceServiceError):
            self.testpythonresourceService.find_by_id(id_to_find)

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_get_testpythonresource_list(self, *args, **kwargs):
        result_collection = self.testpythonresourceService.get_all()
        self.assertTrue(len(result_collection) == 1,
                        "Expected result 1 but got {} ".
                        format(str(len(result_collection))))
        self.assertTrue(result_collection[0]['id'] ==
                        str(self.testpythonresource_data.mongo_id))

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_delete_toolchain_not_system_user(self, *args, **kwargs):
        id_to_delete = str(self.testpythonresource_data.mongo_id)
        with self.assertRaises(TestPythonResourceServiceError) as ex:
            self.testpythonresourceService.delete(id_to_delete)
        self.assertEquals(ex.exception.errors, ErrorCodes.NOT_ALLOWED)

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_delete_toolchain_by_system_user(self, *args, **kwargs):
        id_to_delete = str(self.testpythonresource_data.mongo_id)
        self.testpythonresourceService.auth_context.is_system_user = True
        self.testpythonresourceService.delete(id_to_delete)
        with self.assertRaises(TestPythonResourceServiceError) as ex:
            self.testpythonresourceService.find_by_id(id_to_delete)
        self.assertEquals(ex.exception.errors, ErrorCodes.NOT_FOUND)
        self.testpythonresourceService.auth_context.is_system_user = False

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_delete_toolchain_item_someoneelse(self, *args, **kwargs):
        id_to_delete = str(self.testpythonresource_someoneelses.mongo_id)
        with self.assertRaises(TestPythonResourceServiceError):
            self.testpythonresourceService.delete(id_to_delete)
