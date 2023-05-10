import os

class Hooks:
    def before():
        print("HOOK: before")

    def between():
        print("HOOK: between")
        print("Appending raft file with zeros")
        with open("./data/group/0.raft", "ab") as raftfile:
            raftfile.write(b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0")

    def after():
        print("HOOK: after")
