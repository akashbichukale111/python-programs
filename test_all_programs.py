"""
Automated Test Verification Suite for python-programs repository.
Imports and runs all 15 modules to verify 100% execution pass rate.
"""

import unittest
import importlib

MODULES = [
    "01_basics_and_variables",
    "02_conditional_statements",
    "03_loops_and_iterations",
    "04_string_manipulation",
    "05_lists_and_arrays",
    "06_tuples_and_sets",
    "07_dictionaries",
    "08_functions_and_lambdas",
    "09_file_io_operations",
    "10_exception_handling",
    "11_object_oriented_programming",
    "12_iterators_and_generators",
    "13_decorators_and_closures",
    "14_concurrency_and_asyncio",
    "15_regular_expressions"
]

class TestPythonCurriculum(unittest.TestCase):
    def test_all_15_modules_import_and_execute(self):
        for mod_name in MODULES:
            with self.subTest(module=mod_name):
                mod = importlib.import_module(mod_name)
                self.assertIsNotNone(mod, f"Module {mod_name} should import cleanly")

if __name__ == "__main__":
    unittest.main()
