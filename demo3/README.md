# hooks and runs demo.

This demo demonstrates a new usefull feature for testing with multiple flureedb runs.

The demo at hand simulates a problem that seems to arise with storage on some K8S setups when the system running the pod crashes.
Somehow this crash makes spurious zero bytes to be appended to the raft file. While FlureeDB is not to blame for this, resiliance to
this type of corruption might be possible. The test in this demo checks for this resiliance.

To do this, fsst *dockertest* now has two new parameters. The boolean --hooks flag tells ffst to mount the *hooks* directory and load the *hooks/hooks.py* file as a module.

The hooks.py hools module implements three hooks like this:

```python
import os

class Hooks:
    def before():
        print("HOOK: before")

    def between():
        print("HOOK: between")
        print("Appending raft file with zeros")
        with open("/var/lib/fluree/group/0.raft", "ab") as raftfile:
            raftfile.write(b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0")

    def after():
        print("HOOK: after")
```

The second new commandline argument for *dockertest* is the --runs parameter that defaults to one. 
To run our test, we need to set its vallue to two. Now fsst will try to run the tests twice. 

* Start flureeDB
* Run the test once
* Shut down FlureeDB
* Run the *between* hook
* Start FlureeDB again
* Run the test once more 

```
fsst dockertest --runs 2 --hooks --verbosefluree
```

Nore the --verbosefluree flag. This flag will make fsst put the flureedb logs onto the console.
