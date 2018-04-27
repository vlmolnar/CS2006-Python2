import sys
import unittest

# This function loads the test suites and passes them to the runner
def suite():
    test_cases = [
        "tests.test_refine.RefineTest"
        #"tests.test_analysis.AnalysisTest"
        #"test_visualisation.VisualisationTest"
    ]
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromNames(test_cases)
    return testsuite

# This function builds the tests from the test suite provided
# Currently only one test suit is provided (explained in notebook)
def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity = 2)
    runner.run(testsuite)

# This is used when running the tests from the command line
if __name__ == "__main__":
    test()
