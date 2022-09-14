import PIL.Image as PILImage

from Config.Options import Options


class Image:

    def CreateImage(files, path):

        with PILImage.new("RGB", (Options.images["sizes"]["x"], Options.images["sizes"]["y"])) as image:

            for file in files:

                with PILImage.open(file) as temporary:

                    RGB = PILImage.new("RGB", (0, 0))
                    RGBA = PILImage.new("RGBA", (0, 0))

                    if temporary.size[0] != Options.images["sizes"]["x"] and temporary.size[1] != Options.images["sizes"]["y"]:
                        temporary = temporary.resize(
                            (
                                Options.images["sizes"]["x"],
                                Options.images["sizes"]["y"]
                            )
                        )

                    if temporary.mode == "RGB":
                        RGB = temporary

                    if temporary.mode != "RGB":
                        RGB = temporary.convert("RGB")

                    if temporary.mode == "RGBA":
                        RGBA = temporary

                    if temporary.mode != "RGBA":
                        RGBA = temporary.convert("RGBA")

                    image.paste(RGB, (0, 0), RGBA)

            image.save(path)
            image.close()
