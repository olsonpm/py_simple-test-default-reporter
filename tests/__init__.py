from . import terse


def runTests():
    terse.runTests()


__all__ = ["runTests"]


# ------- #
# Helpers #
# ------- #


def getBaseModuleName(aModule):
    return aModule.__name__.split(".")[-1]
