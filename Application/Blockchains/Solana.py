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


class Solana:
    
    def __main__():
        Utils.Clear()

        FileSystem.CreateDirectory(Options.paths["metadata"])
        FileSystem.CreateDirectory(Options.paths["images"])

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"]))
        }

        Cache.CreateCache(cache["path"])

        print()

        try:
            Solana.Algorithm()

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

            if index == 0:
                Solana.CreateCollection()

            if index != 0:

                if index - 1 == combinations:
                    Utils.Print("All source is already generated.", "green")
                    print()
                    Utils.Print("Total received combinations - {}".format(combinations), "white")
                    Utils.Print("Let's check for the presence of files.", "white")
                    print()
                    Review.__main__()
                    Utils.Exit()

                Solana.CreateDefault(index - 1, combinations)

    def CreateDefault(index, combinations):

        files = FileSystem.GetFiles()
        check = Unique.Verify(files)

        if not check: 
            Utils.Print("{} / {}. This hash already exists - {}".format(index, combinations - 1, Hash.GetHash(files)), "yellow")
            Solana.Algorithm()

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

        cache["value"]["items"][index] = Solana.GenerateMetadataDefault(index, files, "cache")
        metadata["value"] = Solana.GenerateMetadataDefault(index, files, "metadata")

        Cache.ChangeCache(cache["path"], cache["value"])
        Metadata.ChangeMetadata(metadata["path"], metadata["value"])

        Utils.Print("{} / {}. Generating image - {}".format(index, combinations - 1, cache["value"]["items"][index]["hash"]), "green")

        if index == combinations - 1:
            print()

    def GenerateMetadataDefault(index, files, value):

        image = Utils.GetImageURI(index)

        object = {
            "name": "{} #{}".format(Options.name, index + 1),
            "symbol": "{}".format(Options.symbol),
            "description": "{}".format(Options.description),
            "image": image,
            "external_url": "{}".format(Options.external_url),
            "hash": "{}".format(Hash.GetHash(files)),
            "attributes": [],
            "properties": {
                "files": [
                    {
                        "uri": image,
                        "type": "image/{}".format(Options.images["extension"])
                    }
                ]
            }
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

    def CreateCollection():

        files = FileSystem.GetFiles()

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
            "value": {},
        }

        metadata = {
            "path": FileSystem.Resolve(Options.paths["metadata"], "collection.{}".format(Options.metadata["extension"])),
            "value": {},
        }

        image = {
            "path": FileSystem.Resolve(Options.paths["images"], "collection.{}".format(Options.images["extension"]))
        }

        Metadata.CreateMetadata(metadata["path"])
        Image.CreateImage(files, image["path"])

        cache["value"] = Cache.GetCache(cache["path"])
        metadata["value"] = Metadata.GetMetadata(metadata["path"])

        cache["value"]["items"]["-1"] = Solana.GenerateMetadataCollection(files, "cache")
        metadata["value"] = Solana.GenerateMetadataCollection(files, "metadata")

        Cache.ChangeCache(cache["path"], cache["value"])
        Metadata.ChangeMetadata(metadata["path"], metadata["value"])

        Utils.Print("Collection generating - {}".format(cache["value"]["items"]["-1"]["hash"]), "green")
        print()

    def GenerateMetadataCollection(files, value):
        
        image = Utils.GetImageURI("collection")

        object = {
            "name": "{}".format(Options.name),
            "symbol": "{}".format(Options.symbol),
            "description": "{}".format(Options.description),
            "image": image,
            "external_url": "{}".format(Options.external_url),
            "hash": "{}".format(Hash.GetHash(files)),
            "attributes": [],
            "properties": {
                "files": [
                    {
                        "uri": image,
                        "type": "image/{}".format(Options.images["extension"])
                    }
                ]
            }
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
