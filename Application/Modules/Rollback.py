from Application.Modules.Cache import Cache

from Application.Utils.FileSystem import FileSystem
from Application.Utils.Utils import Utils

from Config.Options import Options


class Rollback:

    def __main__():
        Rollback.Algorithm()

    def Algorithm():

        try:

            cache = {
                "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
                "value": "",
            }

            cache["value"] = Cache.GetCache(cache["path"])

            index = Utils.GetLength(cache["value"]["items"])

            if Options.blockchain == "Solana":

                if index == 0:
                    Utils.Print("To prevent an error, we have removed information about the collection.", "yellow")

                if index != 0:
                    Utils.Print("To prevent an error, we have removed information about the number - {}".format(index - 1), "yellow")
                
                metadata = {
                    "default": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index - 1, Options.metadata["extension"])),
                    "collection": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format("collection", Options.metadata["extension"]))
                }

                image = {
                    "default": FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index - 1, Options.images["extension"])),
                    "collection": FileSystem.Resolve(Options.paths["images"], "{}.{}".format("collection", Options.images["extension"]))
                }

                if index == 0:
                    if FileSystem.Exists(metadata["collection"]):
                        FileSystem.Remove(metadata["collection"])

                    if FileSystem.Exists(image["collection"]):
                        FileSystem.Remove(image["collection"])

            if Options.blockchain == "Ethereum":
                Utils.Print("To prevent an error, we have removed information about the number - {}".format(index), "yellow")
                
                metadata = {
                    "default": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"])),
                    "collection": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format("collection", Options.metadata["extension"]))
                }

                image = {
                    "default": FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index, Options.images["extension"])),
                    "collection": FileSystem.Resolve(Options.paths["images"], "{}.{}".format("collection", Options.images["extension"]))
                }
            
            if FileSystem.Exists(metadata["default"]):
                FileSystem.Remove(metadata["default"])

            if FileSystem.Exists(image["default"]):
                FileSystem.Remove(image["default"])

            try:

                if Options.blockchain == "Solana":
                    del cache["value"]["items"][str(index - 1)]
                    Cache.ChangeCache(cache["path"], cache["value"])

                if Options.blockchain == "Ethereum":
                    del cache["value"]["items"][str(index)]
                    Cache.ChangeCache(cache["path"], cache["value"])

            except KeyError:
                return

        except PermissionError:

            if Options.blockchain == "Solana":

                if index == 0:
                    Utils.Print("Insufficient rights to delete file - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format("collection", Options.images["extension"]))), "red")
                    Utils.Print("Delete this file yourself - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format("collection", Options.images["extension"]))), "red")

                if index != 0:
                    Utils.Print("Insufficient rights to delete file - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index - 1, Options.images["extension"]))), "red")
                    Utils.Print("Delete this file yourself - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index - 1, Options.images["extension"]))), "red")

            if Options.blockchain == "Ethereum":
                Utils.Print("Insufficient rights to delete file - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index - 1, Options.images["extension"]))), "red")
                Utils.Print("Delete this file yourself - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index - 1, Options.images["extension"]))), "red")