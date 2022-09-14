class Options:

    name = "AmongUS"
    symbol = "AUS"
    description = "AmongUS is a digital art collection and global community of creators, developers, entrepreneurs, athletes, artists, experimenters and innovators."
    external_url = "https://amongus.com"

    blockchain = "Solana"
    amount = 100

    images = {
        "sizes": {
            "x": 1024,
            "y": 1024
        },

        "uri": "",
        "extension": "png"
    }

    metadata = {
        "extension": "json",
    }

    cache = {
        "extension": "json"
    }

    sorting = [
        "Background",
        "Stand",
        "Backpack",
        "Character",
    ]

    rarity = {
        "Arcane": {
            "weight": 0.606060606
        },
        "Immortal": {
            "weight": 2.424242424
        },
        "Mythical": {
            "weight": 9.696969697
        },
        "Rare": {
            "weight": 29.09090909
        },
        "Common": {
            "weight": 58.18181818
        }
    }

    paths = {
        "layers": "C:\\Users\\liter\\Desktop\\dasdsa\\Layers",

        "images": "C:\\Users\\liter\\Desktop\\dasdsa\\Build\\Images",
        "metadata": "C:\\Users\\liter\\Desktop\\dasdsa\\Build\\Metadata",

        "cache": "C:\\Users\\liter\\Desktop\\dasdsa\\Build"
    }
