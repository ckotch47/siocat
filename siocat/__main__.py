import pyfiglet

from .siocat import *


def main():
    siocat = SioCat()
    print(
        pyfiglet.figlet_format("sio cat"),
        color='c'
    )
    asyncio.run(siocat.run())
