from Application.Modules.Cache import Cache
from Application.Modules.Metadata import Metadata

from Application.Utils.Utils import Utils
from Application.Utils.FileSystem import FileSystem

from Config.Options import Options


class UpdateDescription:

    def __main__():
        UpdateDescription.Algorithm()

    def Algorithm():

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
            "value": {},
        }

        cache["value"] = Cache.GetCache(cache["path"])

        length = Utils.GetLength(cache["value"]["items"])

        for index in range(0, length):

            if Options.blockchain == "Solana":

                if index != length - 1:

                    metadata = {
                        "path": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"])),
                        "value": {},
                    }

                    metadata["value"] = Metadata.GetMetadata(metadata["path"])

                    cache["value"]["items"][str(index)]["description"] = Options.description

                    metadata["value"]["description"] = Options.description

                    Metadata.ChangeMetadata(metadata["path"], metadata["value"])

                    Utils.Print("{}/{} Updated description in file - {}".format(index, length - 2, metadata["path"]), "green")

                    if index == length - 2:
                        print()

                if index == length - 1:

                    metadata = {
                        "path": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format("collection", Options.metadata["extension"])),
                        "value": {},
                    }

                    metadata["value"] = Metadata.GetMetadata(metadata["path"])

                    cache["value"]["items"]["-1"]["description"] = Options.description

                    metadata["value"]["description"] = Options.description

                    Metadata.ChangeMetadata(metadata["path"], metadata["value"])

                    Utils.Print("Collection updated description in file - {}".format(metadata["path"]), "green")

                    if index == length - 1:
                        print()

            if Options.blockchain == "Ethereum":

                metadata = {
                    "path": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"])),
                    "value": {},
                }

                metadata["value"] = Metadata.GetMetadata(metadata["path"])

                cache["value"]["items"][str(index)]["description"] = Options.description

                metadata["value"]["description"] = Options.description

                Metadata.ChangeMetadata(metadata["path"], metadata["value"])

                Utils.Print("{}/{} Updated description in file - {}".format(index, length - 1, metadata["path"]), "green")

                if index == length - 1:
                    print()

        Cache.ChangeCache(cache["path"], cache["value"])

        Utils.Print("Updated description in file - {}".format(cache["path"]), "green")
        Utils.Print("Updated description in all metadata files.", "green")

        print()