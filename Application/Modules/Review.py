from Application.Modules.Cache import Cache

from Application.Utils.Utils import Utils
from Application.Utils.FileSystem import FileSystem

from Config.Options import Options

class Review:

    def __main__():
        Review.Algorithm()

    def Algorithm():

        cache = {
            "path": FileSystem.Resolve(Options.paths["cache"], "cache.{}".format(Options.cache["extension"])),
            "value": {},
        }

        cache["value"] = Cache.GetCache(cache["path"])

        length = Utils.GetLength(cache["value"]["items"])
        
        ImageDirectory = FileSystem.DirectoryFiles(Options.paths["images"])
        MetadataDirectory = FileSystem.DirectoryFiles(Options.paths["metadata"])

        # When the file exists.

        if Utils.GetLength(ImageDirectory) == length and Utils.GetLength(MetadataDirectory) == length:

            for index in range(0, length):

                if Options.blockchain == "Solana":

                    # When the item file exists.

                    if index != length:

                        image = FileSystem.Exists(FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index - 1, Options.images["extension"])))
                        metadata = FileSystem.Exists(FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index - 1, Options.metadata["extension"])))
                    
                        if image and metadata:
                            Utils.Print("{} / {} Image and metadata exist.".format(index - 1, length - 2), "green")
                            
                            if index == length - 1:
                                print()
                                Utils.Print("All metadata has been successfully verified.", "green")

                    # When the collection file exists.
                        
                    if index == length:

                        image = FileSystem.Exists(FileSystem.Resolve(Options.paths["images"], "{}.{}".format("collection", Options.images["extension"])))
                        metadata = FileSystem.Exists(FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format("collection", Options.metadata["extension"])))

                        if image and metadata:
                            Utils.Print("Collection image and metadata exist.", "green")
                                
                            if index == length - 1:
                                Utils.Print("All metadata has been successfully verified.", "green")

                if Options.blockchain == "Ethereum":

                    image = FileSystem.Exists(FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index, Options.images["extension"])))
                    metadata = FileSystem.Exists(FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"])))
                        
                    if image and metadata:
                        Utils.Print("{} / {} Image and metadata exist.".format(index, length - 1), "green")
                                
                        if index == length - 1:
                            print()
                            Utils.Print("All metadata has been successfully verified.", "green")
       
        else:

            # If there is no file in the Images folder.
            
            if Utils.GetLength(ImageDirectory) != length:
                
                for index in range(0, length):
                    
                    if FileSystem.DirectoryFiles(Options.paths["images"]).__contains__("{}.{}".format(index, Options.images["extension"])):

                        if Options.blockchain == "Solana":
                            Utils.Print("{} / {} Image exists.".format(index, length - 2), "green")

                        if Options.blockchain == "Ethereum":
                            Utils.Print("{} / {} Image exists.".format(index, length - 1), "green")
                    
                    if not FileSystem.DirectoryFiles(Options.paths["images"]).__contains__("{}.{}".format(index, Options.images["extension"])):

                        if Options.blockchain == "Solana":

                            if index != length - 1:
                                Utils.Print("{} / {} Image does not exist - {}".format(index , length - 2, FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index, Options.images["extension"]))), "red")
                                Utils.Exit()

                            if index == length - 1:
                                Utils.Print("Collection image does not exist - {}".format(FileSystem.Resolve(Options.paths["images"], "{}.{}".format("collection", Options.images["extension"]))), "red")
                                Utils.Exit()

                        if Options.blockchain == "Ethereum":
                            Utils.Print("{} / {} Image does not exist - {}".format(index , length - 1, FileSystem.Resolve(Options.paths["images"], "{}.{}".format(index, Options.images["extension"]))), "red")
                            Utils.Exit()
            
            # If there is no file in the Metadata folder.

            if Utils.GetLength(MetadataDirectory) != length:
                
                for index in range(0, length):
                    
                    if FileSystem.DirectoryFiles(Options.paths["metadata"]).__contains__("{}.{}".format(index, Options.metadata["extension"])):

                        if Options.blockchain == "Solana":
                            Utils.Print("{} / {} Metadata exists.".format(index, length - 2), "green")

                        if Options.blockchain == "Ethereum":
                            Utils.Print("{} / {} Metadata exists.".format(index, length - 1), "green")

                    if not FileSystem.DirectoryFiles(Options.paths["metadata"]).__contains__("{}.{}".format(index, Options.metadata["extension"])):

                        if Options.blockchain == "Solana":

                            if index != length - 1:
                                Utils.Print("{} / {} Metadata does not exist - {}".format(index, length - 2, FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"]))), "red")
                                Utils.Exit()

                            if index == length - 1:
                                Utils.Print("Collection metadata does not exist - {}".format(FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format("collection", Options.metadata["extension"]))), "red")
                                Utils.Exit()

                        if Options.blockchain == "Ethereum":
                            Utils.Print("{} / {} Metadata does not exist - {}".format(index, length - 1, FileSystem.Resolve(Options.paths["metadata"], "{}.{}".format(index, Options.metadata["extension"]))), "red")
                            Utils.Exit()