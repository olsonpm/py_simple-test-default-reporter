from simple_test_default_reporter.report.explainErrors import border
from textwrap import dedent
from types import SimpleNamespace as obj
from ..noErrorDetails import onlyRootTests as noErrorDetails
import os

onlyRootTests = obj()

onlyRootTests.twoSucceededRootTests = noErrorDetails.twoSucceededRootTests

onlyRootTests.oneFailedOneSucceededRootTests = (
    noErrorDetails.oneFailedOneSucceededRootTests
    + os.linesep
    + dedent(
        f"""
        {border}

        test: fail 2

        the error message

        {border}
        """
    )
    + os.linesep
)
