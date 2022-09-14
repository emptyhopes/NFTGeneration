import json

from Application.Utils.FileSystem import FileSystem
from Application.Utils.Utils import Utils


class Metadata:

    def CreateMetadata(path):

        if FileSystem.Exists(path):
            Utils.Print("Metadata already exists.", "yellow")

        if not FileSystem.Exists(path):

            with open(path, mode="w") as file:
                return json.dump({}, file, indent=2)

    def GetMetadata(path):

        if FileSystem.Exists(path):

            with open(path, mode="r") as file:
                return json.load(file)

        if not FileSystem.Exists(path):
            Utils.Print("Metadata does not exist.", "red")
            Utils.Exit()

    def ChangeMetadata(path, metadata):

        if FileSystem.Exists(path):

            with open(path, mode="w") as file:
                return json.dump(metadata, file, indent=2)

        if not FileSystem.Exists(path):
            Utils.Print("Metadata does not exist.", "red")
            Utils.Exit()
