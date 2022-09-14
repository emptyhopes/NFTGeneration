import os
import random
import termcolor

from Config.Options import Options


class FileSystem:

    def Resolve(*arguments):
        path = ""

        for index, argument in enumerate(arguments):

            if index == 0:
                path = argument

            if index != 0:
                path = path + "\\" + argument

        return path

    def CreateDirectory(path):
        try:

            if os.path.exists(path):
                print(termcolor.colored("The directories already exist.", "yellow"))

            if not os.path.exists(path):
                os.makedirs(path)

        except OSError:
            print(termcolor.colored("Error creating directories.", "red"))

    def GetFiles():
        files = []
        rarities = []
        weights = []

        for rarity in Options.rarity:
            rarities.append(rarity)

        for rarity in Options.rarity:
            weights.append(Options.rarity[rarity]["weight"])

        for layer in Options.sorting:
            rarity = random.choices(rarities, weights=weights, k=1)[0]
            path = FileSystem.Resolve(Options.paths["layers"], layer, rarity)
            index = random.randrange(0, len(os.listdir(path)))
            file = FileSystem.Resolve(path, os.listdir(path)[index])
            files.append(file)

        return files

    def Exists(path):
        return os.path.exists(path)

    def DirectoryFiles(path):
        return os.listdir(path)

    def Remove(path):
        os.remove(path)
