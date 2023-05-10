#!/usr/bin/python3
"""Sample domain-API test script"""
# pylint: disable=unused-argument, no-self-use

class DomainApiTest:
    """Domain-API test class"""
    # pylint: disable=too-few-public-methods
    def __init__(self, test_env):
        """Constructor"""
        self.env = test_env

    async def scenario1(self, domain_api, test_api):
        """The test for transgression one"""
        return True
