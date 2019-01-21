from simple_test_default_reporter.report.explainErrors import border
from textwrap import dedent
from types import SimpleNamespace as obj
from ..noErrorDetails import nestedMess as noErrorDetails
import os

nestedMess = obj()

nestedMess.success = noErrorDetails.success

nestedMess.fail = (
    noErrorDetails.fail
    + os.linesep
    + dedent(
        f"""
        {border}

        test: test 1

        the error message

        {border}

        suite: suite 2
        test: test 4

        the error message

        {border}

        suite: suite 5
        test: test 8

        the error message

        {border}
        """
    )
    + os.linesep
)
