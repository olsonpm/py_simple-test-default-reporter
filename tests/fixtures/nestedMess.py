from types import SimpleNamespace as o
from .helpers import createState, createRootSuite, createASuite, createATest

nestedMess = o()

# ------------------- #
# nestedMess.success  #
# ------------------- #

rootSuite1 = createRootSuite("suite 1", succeeded=True)
suite2 = createASuite("suite 2", succeeded=True, parentSuite=rootSuite1)
suite2.tests = [
    createATest("test 3", succeeded=True, parentSuite=suite2),
    createATest("test 4", succeeded=True, parentSuite=suite2),
]
rootSuite1.suites.append(suite2)

suite3 = createASuite("suite 3", succeeded=True, parentSuite=rootSuite1)
suite3.tests = [createATest("test 5", succeeded=True, parentSuite=suite3)]
rootSuite1.suites.append(suite3)

suite4 = createASuite("suite 4", succeeded=True, parentSuite=suite3)
suite4.tests = [
    createATest("test 6", succeeded=True, parentSuite=suite4),
    createATest("test 7", succeeded=True, parentSuite=suite4),
]
suite3.suites.append(suite4)

rootSuite2 = createRootSuite("suite 5", succeeded=True)
suite6 = createASuite("suite 6", succeeded=True, parentSuite=rootSuite2)
suite6.tests = [createATest("test 8", succeeded=True, parentSuite=suite6)]
rootSuite2.suites.append(suite6)

nestedMess.success = createState(
    rootTests=[
        createATest("test 1", succeeded=True),
        createATest("test 2", succeeded=True),
    ],
    rootSuites=[rootSuite1, rootSuite2],
    succeeded=True,
)

# --------------- #
# nestedMess.fail #
# --------------- #

rootSuite1 = createRootSuite("suite 1", succeeded=False)
suite2 = createASuite("suite 2", succeeded=False, parentSuite=rootSuite1)
suite2.tests = [
    createATest("test 3", succeeded=True, parentSuite=suite2),
    createATest("test 4", succeeded=False, parentSuite=suite2),
]
rootSuite1.suites.append(suite2)

suite3 = createASuite("suite 3", succeeded=False, parentSuite=rootSuite1)
suite3.tests = [createATest("test 5", succeeded=True, parentSuite=suite3)]
rootSuite1.suites.append(suite3)

suite4 = createASuite("suite 4", succeeded=True, parentSuite=suite3)
suite4.tests = [
    createATest("test 6", succeeded=True, parentSuite=suite4),
    createATest("test 7", succeeded=True, parentSuite=suite4),
]
suite3.suites.append(suite4)

suite5 = createASuite("suite 5", succeeded=False, parentSuite=suite3)
suite5.tests = [createATest("test 8", succeeded=False, parentSuite=suite5)]
suite3.suites.append(suite5)

rootSuite2 = createRootSuite("suite 6", succeeded=True)
suite7 = createASuite("suite 7", succeeded=True, parentSuite=rootSuite2)
suite7.tests = [createATest("test 10", succeeded=True, parentSuite=suite7)]
rootSuite2.suites.append(suite7)

nestedMess.fail = createState(
    rootTests=[
        createATest("test 1", succeeded=False),
        createATest("test 2", succeeded=True),
    ],
    rootSuites=[rootSuite1, rootSuite2],
    succeeded=False,
)
