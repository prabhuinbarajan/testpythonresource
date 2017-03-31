#!/usr/bin/python
"""
Add docstring here
"""
import time
import unittest

import mock

from mock import patch
import mongomock


class TestTestPythonResourceModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("before class")

    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def test_create_testpythonresource_model(self):
        from qube.src.models.testpythonresource import TestPythonResource
        testpythonresource_data = TestPythonResource(name='testname')
        testpythonresource_data.tenantId = "23432523452345"
        testpythonresource_data.orgId = "987656789765670"
        testpythonresource_data.createdBy = "1009009009988"
        testpythonresource_data.modifiedBy = "1009009009988"
        testpythonresource_data.createDate = str(int(time.time()))
        testpythonresource_data.modifiedDate = str(int(time.time()))
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            testpythonresource_data.save()
            self.assertIsNotNone(testpythonresource_data.mongo_id)
            testpythonresource_data.remove()

    @classmethod
    def tearDownClass(cls):
        print("After class")


if __name__ == '__main__':
    unittest.main()
