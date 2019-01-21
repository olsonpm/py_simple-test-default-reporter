# ------- #
# Imports #
# ------- #

from contextlib import redirect_stdout
from difflib import Differ
from os import path
from simple_test_default_reporter.fns import joinWith, passThrough
import io


# ---- #
# Init #
# ---- #

_d = Differ()
fixturesDir = path.join(path.dirname(__file__), "fixtures")


# ---- #
# Main #
# ---- #


def diff(left, right):
    result = _d.compare(
        left.splitlines(keepends=True), right.splitlines(keepends=True)
    )
    return passThrough(result, [list, joinWith("")])


def getActualOut(fn):
    f = io.StringIO()
    with redirect_stdout(f):
        fn()
    return f.getvalue()
