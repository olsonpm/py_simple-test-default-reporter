from ..Results import Results
from . import noErrorDetails, withErrorDetails


def runTests():
    r = Results("no error details")
    noErrorDetails.runTests(r).printResults()

    r = Results("with error details")
    withErrorDetails.runTests(r).printResults()


__all__ = ["runTests"]


# ------- #
# Helpers #
# ------- #


def getBaseModuleName(aModule):
    return aModule.__name__.split(".")[-1]
