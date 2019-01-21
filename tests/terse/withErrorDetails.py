# ------- #
# Imports #
# ------- #

from simple_test_default_reporter import report
from simple_test_default_reporter.fns import passThrough
from .. import fixtures
from ..utils import diff, getActualOut
from .expected import withErrorDetails as expected


# ---- #
# Main #
# ---- #


def runTests(r):
    return passThrough(r, [onlyRootTests, oneRootSuite, nestedMess])


def onlyRootTests(r):
    actualOut = getActualOut(
        lambda: report(fixtures.onlyRootTests.twoSucceededRootTests)
    )
    expectedOut = expected.onlyRootTests.twoSucceededRootTests
    if actualOut != expectedOut:
        r.addError("onlyRootTests.twoSucceededRootTests report failed")

    actualOut = getActualOut(
        lambda: report(fixtures.onlyRootTests.oneFailedOneSucceededRootTests)
    )
    expectedOut = expected.onlyRootTests.oneFailedOneSucceededRootTests
    if actualOut != expectedOut:
        print(diff(actualOut, expectedOut))
        r.addError("onlyRootTests.oneFailedOneSucceededRootTests report failed")

    return r


def oneRootSuite(r):
    actualOut = getActualOut(lambda: report(fixtures.oneRootSuite.success))
    expectedOut = expected.oneRootSuite.success
    if actualOut != expectedOut:
        r.addError("oneRootSuite.success report failed")

    actualOut = getActualOut(lambda: report(fixtures.oneRootSuite.fail))
    expectedOut = expected.oneRootSuite.fail
    if actualOut != expectedOut:
        r.addError("oneRootSuite.fail report failed")

    return r


def nestedMess(r):
    actualOut = getActualOut(lambda: report(fixtures.nestedMess.success))
    expectedOut = expected.nestedMess.success
    if actualOut != expectedOut:
        r.addError("nestedMess.success report failed")

    actualOut = getActualOut(lambda: report(fixtures.nestedMess.fail))
    expectedOut = expected.nestedMess.fail
    if actualOut != expectedOut:
        r.addError("nestedMess.fail report failed")

    return r
