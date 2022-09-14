from Application.Blockchains.Solana import Solana
from Application.Blockchains.Ethereum import Ethereum

from Application.Utils.Utils import Utils

from Config.Options import Options

class Application:

    def __main__():

        if Options.blockchain == "Solana":
            Solana.__main__()

        if Options.blockchain == "Ethereum":
            Ethereum.__main__()

        else:
            Utils.Print("Error reading blockchain from Options.", "red")
            Utils.Exit()