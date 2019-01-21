from types import SimpleNamespace as o
from simple_test_default_reporter.fns import iif, noop


def createState(*, succeeded, rootTests=[], rootSuites=[], currentSuite=None):
    return o(
        rootTests=rootTests,
        rootSuites=rootSuites,
        currentSuite=currentSuite,
        succeeded=succeeded,
    )


def createRootSuite(label, *, succeeded):
    return o(
        label=label,
        fn=noop,
        tests=[],
        suites=[],
        parentSuite=None,
        succeeded=succeeded,
    )


def createASuite(label, *, succeeded, parentSuite):
    return o(
        label=label,
        fn=noop,
        tests=[],
        suites=[],
        parentSuite=parentSuite,
        succeeded=succeeded,
    )


def createATest(label, *, error=None, parentSuite=None, succeeded):
    aTest = o(
        fn=noop, label=label, parentSuite=parentSuite, succeeded=succeeded
    )

    if not succeeded:
        aTest.error = iif(error is None, Exception("the error message"), error)

    return aTest


def createTests(label, *, error=None, parentSuite=None, succeeded):
    tests = [
        o(label=label, fn=noop, parentSuite=parentSuite, succeeded=succeeded)
    ]

    if not succeeded:
        tests[0].error = iif(
            error is None, Exception("the error message"), error
        )

    parentSuite.tests = tests

    return tests
