from types import SimpleNamespace as obj
from simple_test_default_reporter.report.utils import o, x

onlyRootTests = obj()

onlyRootTests.twoSucceededRootTests = f"""\
success 1 {o}
success 2 {o}
"""

onlyRootTests.oneFailedOneSucceededRootTests = f"""\
success 1 {o}
fail 2 {x}
"""
