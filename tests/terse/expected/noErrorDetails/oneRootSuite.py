from types import SimpleNamespace as obj
from simple_test_default_reporter.report.utils import o, x

oneRootSuite = obj()

oneRootSuite.success = f"""\
suite 1 {o}
"""

oneRootSuite.fail = f"""\
suite 1 {x}
    test 1 {x}
"""
