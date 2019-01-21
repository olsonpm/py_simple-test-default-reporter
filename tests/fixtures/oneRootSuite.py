from types import SimpleNamespace as o
from .helpers import createState, createRootSuite, createTests

oneRootSuite = o()

successSuite = createRootSuite("suite 1", succeeded=True)
successTests = createTests("test 1", parentSuite=successSuite, succeeded=True)
rootSuccessSuites = [successSuite]

failSuite = createRootSuite("suite 1", succeeded=False)
failTests = createTests("test 1", parentSuite=failSuite, succeeded=False)
rootFailSuites = [failSuite]

oneRootSuite.success = createState(rootSuites=rootSuccessSuites, succeeded=True)
oneRootSuite.fail = createState(rootSuites=rootFailSuites, succeeded=False)
