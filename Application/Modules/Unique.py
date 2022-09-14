from Application.Modules.Cache import Cache

from Application.Utils.FileSystem import FileSystem
from Application.Utils.Hash import Hash

from Config.Options import Options

class Unique:

    def Verify(files):

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
            "value": "",
        }

        cache["value"] = Cache.GetCache(cache["path"])

        hash = Hash.GetHash(files)

        for index in cache["value"]["items"]:

            if hash == cache["value"]["items"][index]["hash"]:
                return False

        return True
