#!/usr/bin/python3
"""Sample domain-API test script"""
# pylint: disable=unused-argument, no-self-use

class DomainApiTest:
    """Domain-API test class"""
    # pylint: disable=too-few-public-methods
    def __init__(self, test_env):
        """Constructor"""
        self.env = test_env

    async def run_test_give_role(self, domain_api, test_api):
        """The test for allowed promtions"""
        for personpower in [
                ["artist", "judicial"],
                ["farmer", "executive"],
                ["baker", "legislator"]]:
            print(personpower)
            trans = domain_api["role"].give_role(
                    person=personpower[0],
                    power=personpower[1])
            await trans()
        return True

    async def scenario1(self, domain_api, test_api):
        """The test for transgression one"""
        print(["judge", "executive"])
        trans = domain_api["role"].give_role(
                    person="judge",
                    power="executive")
        try:
            await trans()
        except:
            return True
        return False, "Shouldn't be able to give a judge executive powers"

    async def scenario2(self, domain_api, test_api):
        """The test for transgression two"""
        print(["judge", "legislator"])
        trans = domain_api["role"].give_role(
                    person="judge",
                    power="legislator")
        try:
            await trans()
        except:
            return True
        return False, "Shouldn't be able to give a judge legislative powers"

    async def scenario3(self, domain_api, test_api):
        """The test for transgression three"""
        print(["minister", "judicial"])
        trans = domain_api["role"].give_role(
                    person="minister",
                    power="judicial")
        try:
            await trans()
        except:
            return True
        return False, "Shouldn't be able to give a minister judicial powers"

    async def scenario4(self, domain_api, test_api):
        """The test for transgression four"""
        print(["minister", "legislator"])
        trans = domain_api["role"].give_role(
                    person="minister",
                    power="legislator")
        try:
            await trans()
        except:
            return True
        return "Shouldn't be able to give a minister legislative powers"

    async def scenario5(self, domain_api, test_api):
        """The test for transgression five"""
        print(["senator", "executive"])
        trans = domain_api["role"].give_role(
                    person="senator",
                    power="executive")
        try:
            await trans()
        except:
            return True
        return False, "Shouldn't be able to give a senator executive powers"

    async def scenario6(self, domain_api, test_api):
        """The test for transgression six"""
        print(["senator", "judicial"])
        trans = domain_api["role"].give_role(
                    person="senator",
                    power="judicial")
        try:
            await trans()
        except:
            return True
        return False, "Shouldn't be able to give a senator judicial powers"

