from types import SimpleNamespace as obj
from simple_test_default_reporter.report.utils import o, x

nestedMess = obj()

nestedMess.success = f"""\
test 1 {o}
test 2 {o}

suite 1 {o}
    suite 2 {o}
    suite 3 {o}
        suite 4 {o}

suite 5 {o}
    suite 6 {o}
"""

nestedMess.fail = f"""\
test 1 {x}
test 2 {o}

suite 1 {x}
    suite 2 {x}
        test 4 {x}

    suite 3 {x}
        suite 4 {o}
        suite 5 {x}
            test 8 {x}

suite 6 {o}
    suite 7 {o}
"""
