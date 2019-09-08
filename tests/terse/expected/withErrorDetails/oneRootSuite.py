from simple_test_default_reporter.report.explainErrors import border
from textwrap import dedent
from types import SimpleNamespace as obj
from ..noErrorDetails import oneRootSuite as noErrorDetails
import os

oneRootSuite = obj()

oneRootSuite.success = noErrorDetails.success

oneRootSuite.fail = (
    noErrorDetails.fail
    + os.linesep
    + dedent(
        f"""
        {border}

        suite: suite 1
        test: test 1

        a formatted exception

        {border}
        """
    )
    + os.linesep
)
