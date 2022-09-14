from Application.Modules.Cache import Cache

from Application.Utils.Utils import Utils
from Application.Utils.FileSystem import FileSystem

from Config.Options import Options

class Percentage:
    def __main__():

        for layer in FileSystem.DirectoryFiles(Options.paths["layers"]):

            (files, counts) = Percentage.Algorithm(layer)

            for index, file in enumerate(files):
                temporary = ""

                for rarity in Options.rarity:
                    if FileSystem.DirectoryFiles(FileSystem.Resolve(Options.paths["layers"], layer, rarity)).__contains__("{}.{}".format(file, Options.images["extension"])):
                        temporary = rarity

                Utils.Print("{}/{}/{}.{} - {}% have this trait.".format(layer, temporary, file, Options.images["extension"], counts[index]), "cyan")

            print()

    def Algorithm(layer):

        files = []
        counts = []

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
            "value": {},
        }

        cache["value"] = Cache.GetCache(cache["path"])

        length = Utils.GetLength(cache["value"]["items"])

        for rarity in Options.rarity:
            path = FileSystem.Resolve(Options.paths["layers"], layer, rarity)
            files.extend(FileSystem.DirectoryFiles(path))
            
        for index, value in enumerate(files):
            files[index] = value.split(".")[0]
            counts.append(0)

        for index in range(0, length):

            if Options.blockchain == "Solana":

                if index == 0:

                    for attribute in cache["value"]["items"]["-1"]["attributes"]:
                        if attribute["trait_type"] == layer:
                            for i, value in enumerate(files):
                                if attribute["value"] == value:
                                    counts[i] = counts[i] + 1

                if index != 0:

                    for attribute in cache["value"]["items"][str(index - 1)]["attributes"]:
                        if attribute["trait_type"] == layer:
                            for i, value in enumerate(files):
                                if attribute["value"] == value:
                                    counts[i] = counts[i] + 1

            if Options.blockchain == "Ethereum":

                for attribute in cache["value"]["items"][str(index)]["attributes"]:
                    if attribute["trait_type"] == layer:
                        for i, value in enumerate(files):
                            if attribute["value"] == value:
                                counts[i] = counts[i] + 1

        for index, count in enumerate(counts):
            if (count != 0):
                counts[index] = round((count / length) * 100, 2)

        return (files, counts)