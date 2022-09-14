import os
import sys
import termcolor

from Application.Utils.FileSystem import FileSystem

from Config.Options import Options


class Utils:

    def GetCombinations():
        combinations = 1

        for layer in os.listdir(Options.paths["layers"]):
            temporary = 0

            for rarity in Options.rarity:
                path = FileSystem.Resolve(Options.paths["layers"], layer, rarity)
                temporary = temporary + Utils.GetLength(os.listdir(path))

            combinations = combinations * temporary

        return combinations

    def GetImageURI(value):
        image = "{}{}.{}".format(Options.images["uri"], value, Options.images["extension"])
        length = Utils.GetLength(Options.images["uri"])

        if not length == 0:
            image = "{}/{}.{}".format(Options.images["uri"], value, Options.images["extension"])

        return image

    def GetLength(object):
        return len(object)

    def GetString(string):
        return str(string)

    def Clear():
        os.system("cls")

    def Print(message, color):
        print(termcolor.colored(message, color))

    def Exit():
        sys.exit(0)
