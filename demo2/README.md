# Demo 2 fsst

The files in this directory are meant to demo smart function testing using the [trias politica](https://en.wikipedia.org/wiki/Separation_of_powers) as an example.

### setup

We define three roles in the build in fluree _\_role_ collection:

* legislator
* executive
* judicial

And we define six users

* senator
* minister
* judge
* baker
* farmer
* artist

Three of the users get a predefined role

* senator : legislator
* minister : executive
* judge : judicial


### the test

To test, we create a test that at first fails because there are no smart functions. The test consists of two parts.

#### positive test

The first part of the test should always succeed. Here we give a role to each of the users withour a current role:

* artist : judicial
* farmer : executive
* baker : legislator

This should all be allowed.

#### negative test

Now for the tests that should actually fail if the trias politica is properly inforced

* judge : executive
* judge : legislator
* minister : judicial
* minister : legislator
* senator : executive
* senator : judicial

### Running the test without constraints

First we run the test with no constrains at all:

```
fsst dockertest
```

This test should fail as nothing is constrainig the updates.

### Running the tests with constraints

There is a second target defined in build.json that defines a second stage. This **CURRENTLY BROKEN** stage tries to put constraints on the roles predicate in order to make the restricted updated really impossible. We call fsst dockertest with two extra arguments.

```
fsst dockertest --target repaired --stages enforce_trias_politica
```


