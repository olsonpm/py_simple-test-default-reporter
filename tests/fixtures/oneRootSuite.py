from types import SimpleNamespace as o
from .helpers import createState, createRootSuite, createTests

oneRootSuite = o()

successSuite = createRootSuite("suite 1", succeeded=True)
successTests = createTests("test 1", parentSuite=successSuite, succeeded=True)
rootSuccessSuites = [successSuite]

failSuite = createRootSuite("suite 1", succeeded=False)
failTests = createTests(
    "test 1",
    formattedException="a formatted exception",
    parentSuite=failSuite,
    succeeded=False,
)
rootFailSuites = [failSuite]

oneRootSuite.success = createState(suites=rootSuccessSuites, succeeded=True)
oneRootSuite.fail = createState(suites=rootFailSuites, succeeded=False)
