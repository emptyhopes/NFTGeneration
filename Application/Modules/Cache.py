import json

from Application.Utils.FileSystem import FileSystem
from Application.Utils.Utils import Utils


class Cache:

    def CreateCache(path):

        if FileSystem.Exists(path):
            Utils.Print("Cache already exists.", "yellow")

        if not FileSystem.Exists(path):

            with open(path, mode="w") as file:
                return json.dump({"items": {}}, file, indent=2)

    def GetCache(path):

        if FileSystem.Exists(path):

            with open(path, mode="r") as file:
                return json.load(file)

        if not FileSystem.Exists(path):
            Utils.Print("Cache does not exist.", "red")
            Utils.Exit()

    def ChangeCache(path, cache):

        if FileSystem.Exists(path):

            with open(path, mode="w") as file:
                return json.dump(cache, file, indent=2)

        if not FileSystem.Exists(path):
            Utils.Print("Cache does not exist.", "red")
            Utils.Exit()