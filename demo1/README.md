# Test for a collection spec that tries to prohibit deletion when deletion leads to a missing ref

To run this test with fsst run:
```
fsst dockertest --linger
```

The **flure_parts** dir contains a schema with three collections and a smart function bound to one of the collections:

* class : Classes a student can take
* student: The students
* enrolement: Links classes to students
* a smart function enrolementHasStudent that implements the spec  of the enrolement collection.

The test scenario is ass follows:

* Two classes are created, English and Spanish
* Two students are created, Alice and Bob
* Alice and Bob are enroled into English class.
* A two step delete for the Alice student is initiated by querying all of Allice her enrolements
* To simulate a race condition, Alice is enroled into Spanish class.
* A transaction for deleting Alice and her enrolements is created, because of the race condition her Spanish class enrolement is missing from  the transaction.
* The transaction SHOULD fail because of the collection spec smart function.
* The two step delete for the Alice student is initiated a second time by querying all of Allice her enrolements
* A transaction for deleting Alice and her enrolements is created and executed, this should succeed.

At the time of writing, the first transaction doesn't fail, leaving a Spanish class enrolement without a student ref when Alice has been deleted.

# Usefull queries

```json
{
  "select": [
    "*",
    {"enroled_class": ["*"]},
    {"enroled_student": ["*"]}
  ],
  "from": "enrolement"
}
```

```json
{
  "select": [
    "*",
    {"spec": ["*"]}
  ],
  "from": "_collection"
}
```
