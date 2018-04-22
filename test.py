import sys
import unittest

def suite():
    test_cases = [
        "tests.test_refine.RefineTest"
        #"tests.test_analysis.AnalysisTest"
        #"test_visualisation.VisualisationTest"
        #"test_map.MapTest"
    ]
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromNames(test_cases)
    return testsuite

def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity = 2)
    runner.run(testsuite)

if __name__ == "__main__":
    test()
