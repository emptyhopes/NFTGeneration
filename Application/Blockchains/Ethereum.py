from Application.Modules.Cache import Cache
from Application.Modules.Image import Image
from Application.Modules.Review import Review
from Application.Modules.Unique import Unique
from Application.Modules.Metadata import Metadata
from Application.Modules.Rollback import Rollback

from Application.Utils.Hash import Hash
from Application.Utils.Utils import Utils
from Application.Utils.FileSystem import FileSystem

from Config.Options import Options


class Ethereum:
    
    def __main__():
        Utils.Clear()

        FileSystem.CreateDirectory(Options.paths["metadata"])
        FileSystem.CreateDirectory(Options.paths["images"])

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"]))
        }

        Cache.CreateCache(cache["path"])

        try:
            Ethereum.Algorithm()

        except KeyboardInterrupt:
            Rollback.__main__()
            Utils.Exit()

        except RecursionError:
            Utils.Print("The memory stack was full restart the software.", "red")
            Rollback.__main__()
            Utils.Exit()

    def Algorithm():

        while True:

            combinations = Utils.GetCombinations()

            if Options.amount != 0:
                combinations = Options.amount

            cache = Cache.GetCache(FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])))
            index = Utils.GetLength(cache["items"])

            if index == combinations:
                print()
                Utils.Print("All source is already generated.", "green")
                print()
                Utils.Print("Total received combinations - {}".format(combinations), "white")
                Utils.Print("Let's check for the presence of files.", "white")
                print()
                Review.__main__()
                Utils.Exit()

            Ethereum.CreateDefault(index, combinations)

    def CreateDefault(index, combinations):

        files = FileSystem.GetFiles()
        check = Unique.Verify(files)

        if not check: 
            Utils.Print("{} / {}. This hash already exists - {}".format(index, combinations - 1, Hash.GetHash(files)), "yellow")
            Ethereum.Algorithm()

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
            "value": {},
        }

        metadata = {
            "path": FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"])),
            "value": {},
        }

        image = {
            "path": FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index, Options.images["extension"]))
        }

        Metadata.CreateMetadata(metadata["path"])
        Image.CreateImage(files, image["path"])

        cache["value"] = Cache.GetCache(cache["path"])
        metadata["value"] = Metadata.GetMetadata(metadata["path"])

        cache["value"]["items"][index] = Ethereum.GenerateMetadataDefault(index, files, "cache")
        metadata["value"] = Ethereum.GenerateMetadataDefault(index, files, "metadata")

        Cache.ChangeCache(cache["path"], cache["value"])
        Metadata.ChangeMetadata(metadata["path"], metadata["value"])

        Utils.Print("{} / {}. Generating image - {}".format(index, combinations - 1, cache["value"]["items"][index]["hash"]), "green")

    def GenerateMetadataDefault(index, files, value):

        image = Utils.GetImageURI(index)

        object = {
            "name": "{} #{}".format(Options.name, index + 1),
            "description": "{}".format(Options.description),
            "image": image,
            "hash": "{}".format(Hash.GetHash(files)),
            "attributes": []
        }

        for file in files:
            
            object["attributes"].append({
                "trait_type": file.split("\\")[-3],
                "rarity": file.split("\\")[-2],
                "value": file.split("\\")[-1].split(".{}".format(Options.images["extension"]))[0]
            })

        if value == "metadata":

            del object["hash"]

            for index in range(0, Utils.GetLength(object["attributes"])):
                del object["attributes"][index]["rarity"]

        return object