# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.comment_annotation import CommentAnnotation

class TestCommentAnnotation(unittest.TestCase):
    """CommentAnnotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentAnnotation:
        """Test CommentAnnotation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentAnnotation`
        """
        model = CommentAnnotation()
        if include_optional:
            return CommentAnnotation(
                id = '',
                text = '',
                codes = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return CommentAnnotation(
                id = '',
                text = '',
        )
        """

    def testCommentAnnotation(self):
        """Test CommentAnnotation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
