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
        """Scenario where we create a user and a contact and link them"""
        print(list(domain_api.keys()))
        print("######################################################################################")
        transaction = test_api["role"].create_class(class_name="English")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't create English class"
        print("Created English class")
        transaction = test_api["role"].create_class(class_name="Spanish")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't create Spanish class"
        print("Created Spanish class")
        transaction = test_api["role"].create_student(student_name="Alice")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't create student Alice"
        print("Created student Alice")
        transaction = test_api["role"].create_student(student_name="Bob")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't create student Bob"
        print("Created student Bob")
        transaction = test_api["role"].enrole_student(class_name="English", student_name="Alice")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't enrole Alice in English class"
        print("Enroled Alice in English class")
        transaction = test_api["role"].enrole_student(class_name="English", student_name="Bob")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't enrole Bob in English class"
        print("Enroled Bob in English class")
        response = await test_api["role"].get_enrolements(student_name="Alice")
        enrolement_id = set()
        for subresponse in response:
            enrolement_id.add(subresponse[0])
        if len(enrolement_id) != 1:
            return False, "Expected one class enolements for Alice, got " + str(len(cccid)) 
        print("DEBUG: Fetched list of Alice her enrolements pre-race-condition")
        transaction = test_api["role"].enrole_student(class_name="Spanish", student_name="Alice")
        all_ok = await transaction()
        if not all_ok:
            return False, "Couldn't enrole Alice in Spanish class"
        print("DEBUG: Created race condition by enroling Alice in Spanish class in the middle of trying to delete Alice as a student.")
        # First test deleting a contact that should fail because of race condition
        transaction = test_api["role"].delete_student(student_name="Alice")
        for delete_id in enrolement_id:
            transaction.delete_enrolement(enrid=delete_id)
        print("DEBUG:", transaction.transaction)
        all_ok = await transaction()
        if all_ok:
            print(all_ok)
            return False, "Successfully deleted student Alice, this should NOT have been possible due to the Spanish class enrolement race condition."
        # Now one that should succeed
        response = await test_api["role"].get_enrolements(student_name="Alice")
        enrolement_id = set()
        for subresponse in response:
            enrolement_id.add(subresponse[0])
        if len(enrolement_id) != 2:
            return False, "Expected two class enrolements for Alice, got " + str(len(cccid))
        transaction = test_api["role"].delete_student(student_name="Alice")
        for delete_id in enrolement_id:
            transaction.delete_enrolement(enrid=delete_id)
        all_ok = await transaction()
        if not all_ok:
            return False, "Deleting Alice without the racecondition failed"
        print("######################################################################################")
        return True, "Simple scenario OK"

