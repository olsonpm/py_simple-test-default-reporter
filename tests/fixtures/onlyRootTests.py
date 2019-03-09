from types import SimpleNamespace as o
from .helpers import createState, createATest

onlyRootTests = o()

onlyRootTests.twoSucceededRootTests = createState(
    succeeded=True,
    tests=[
        createATest("success 1", succeeded=True),
        createATest("success 2", succeeded=True),
    ],
)

onlyRootTests.oneFailedOneSucceededRootTests = createState(
    succeeded=False,
    tests=[
        createATest("success 1", succeeded=True),
        createATest("fail 2", succeeded=False),
    ],
)
