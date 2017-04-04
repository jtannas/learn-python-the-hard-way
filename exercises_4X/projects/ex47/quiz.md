# Study Drills

## Go read about nosetests more, and also read about alternatives.

Video: [Andrew Knight | Testing is Fun in Python](https://www.youtube.com/watch?v=Sb2tz9Hlbp8).

Nose extends unittest to make testing easier. It lets you write test either
with a testcase class or with functions.
- Test class methods and test functions should be named "test_*".
- Node test classes do not need to inherit from any superclass.
- Recommended to use test functions over test classes.
- Handles parameters.
- Backwards compatible - can run unittest or doctest files.
- Some plugins may not work with Python3.
- Nose is no longer actively supported.

Nose directory:

    <root dir>
    |-- <product packages>
    |-- tests
    |   `-- test_<names>.py
    |-- nose.cfg                (optional)
    `-- README.md
Note how the tests directory does not require an __init__.py (aka it does not
have to be a python package. The nose.cfg is an optional file.

Example nose tests

    from example.calc_func import *
    from nose.tools import raises

    ...

    # Basic test function
    def test_add():
        value = add(NUMBER_1, NUMBER_2)
        assert value == 5.0

    # Testing an exception
    @raises(ZeroDivisionError)
    def test_divide_by_zero():
        divide(NUMBER_1, 0)

    # Private helper function for test generator
    def _check_maximum(a, b):
        assert maximum(a, b) == NUMBER_1

    # Test generator
    def test_maximum():
        for a, b in [(N1, N2), (N2, N1), (N1, N1)]:
            yield _check_maximum, a, b

nose example launch

    # Run from the root directory of the Python project
    > cd example-unit-python-nose

    # Run all tests discoverable
    > nosetests

    # Run all tests in a module
    > nosetests tests.test_calc_func

    # Run a specific test function
    > nosetests tests.test_calc_func:test_add

    # Run a specific test class
    > nosetests tests.module:ClassName

    # Generate xUnit-style XML report for results
    # --xunit-file" is optional (default value shown)
    > nosetests --with-xunit --xunit-file-nosetests.xml

### Others (excluding doctest)

#### Pytest
The favored, modern python testing tool. Plugins allowed for extending it.
Pytest example directory:

    <root dir>
    |-- <product packages>
    |-- tests
    |   |-- test_<names>.py      *** NO __INIT__.py FILE***
    |   |-- <names>_test.py
    |-- setup.py
    |-- pytest.ini              (optional)
    `-- README.md

Pytest example code:

    import pytest
    from example.calc_func import *

    ...

    def test_add();
        value =add(NUMBER_1, NUMBER_2)
        assert value == 5.0

    def test_divide_by_zero():
        with pytest.raises(ZeroDivisionError):
            divide(NUMBER_1, 0)

    @pytest.mark.parametrize("a,b,expected", [
        (NUMBER_1, NUMBER_2, NUMBER_1),
        (NUMBER_2, NUMBER_1, NUMBER_1),
        (NUMBER_1, NUMBER_1, NUMBER_1),
    ])
    def test_maximum(a, b, expected):
        asset maximum(a, b) == expected

Pytest example launch:

    # Run from the root directory of the Python project
    > cd example-unit-python-pytest

    # Make sure modules are in the Python path
    > PYTHONPATH=.

    # Run all tests
    > py.test

    # List all test with results as they are run
    > py.test -v

    # Run all tests under a given path
    > py.test -v

    # Run all test in a module
    > py.test tests/test_calc_func.py

    # Generate JUnit XML report for results
    > py.test --junitxml-<path>

    # Generate code coverage reports
    # Must have pytest-cov installed
    > py.test <test path>
        --cov=<product code path> \
        --cov-report-term \
        --cov-report-xml \
        --cov-report-html

    # Command help
    py.test -h

    # Calling directly from python
    > python -m pytest

#### Avocado
- Can run test written in any language, including bash and C
- In Python, each test must be an avocado.Test subclass
- Each test method in the class must be named "test_*".
- Has standard setup and cleanup methods
- The test class also has special attribute:
    - whiteboard is a string that will be saved automatically to test results
    - params is a way to access test parameters and can be multiplexed
    - log is a convenient logger
- Advanced features including:
    - parameter multiplexing
    - test discovery
    - result formatting
    - job replay
    - remote test runs
    - GDB debugging
    - plugins
- Linux only

Avocado example directory:

    <root dir>
    |-- <product packages>
    |-- tests
    |   |-- test_<names>.py
    `-- README.md

    Avocado does not require a specific directory layout because it discovers all tests
    within a directory. Nevertheless, it is recommended to seperate test files into
    their own directory.

Avocado example code:

    from avocado import Test
    from example.calc import Calculator

    ...

    class CalculatorTest(Test):
        def setUp(self):
            self.calc = Calculator()

        # Helper methods

        def chack_value(self, actual, expected):
            val_str = "value = %s" % actual
            self.whiteboard = val_str
            self.log.debug(val_strr)
            self.assertEquals(actual, expected, FAILURE)

        def get_values(self):
            a = self.params.get("a", path="/values/*", default=NUMBER_1)
            b = self.params.get("b", path="/values/*", default=NUMBER_2)
            return a, b

        # Basic test method

        def test_add(self):
            value = self.calc.add(NUMBER_1, NUMBER_2)
            self.check_value(value, 5.0)

        # Test method with multiplexed parameters
        # Notes: When multiplexing, all test methods are run
        #        for each parameter combination

        def test_subtract(self):
            a, b = self.get_values()
            actual = self.calc.subtract(a, b)
            expected = a - b
            self.check_value(actual, expected)

Avocado example launch:

    #  Run from the root directory of the python project
    > cd example-unit-python-avocado

    # Export the Python path
    > export PYTHONPATH=.

    # Discover and list tests under a given path
    > avocado list <path>

    # Simulate a run with parameters and options
    > avocado run <path> --dry-run

    # Actually run all tests under a given path
    > avocado run <path>

    # Running with multiplexed parameters
    > avocado run <path> -- multiplex <YAML file>

    # Exit testing on the first failure
    > avocado run <path> --failfast

    # Rerun the latest job
    > avocado run --replay latest

    # Rerun any job using the hash ID printed for the job
    > avocado run --replay <hash ID>

    # Open browser to show HTML test report after run
    # Note: every run generates an HTML report and prints the URL
    > avocado run <path> --open-browser

    # Generate xunit XML report
    > avocado run <path> --xunit <XML file path or "-">
## Learn about Python's "doc tests" and see if you like them better.

They are neat, but they don't seem to be suitable for complicated code.
I'd happily use them for fairly simple functions, but not for much else.

doctest Example code:

    def subtract(a, b):
        """Subtracts two numbers

        >>> subtract(3, 2)
        1
        >>> subtract(2, 3)
        -1
        """
        return a - b

doctest directory layout:

    <root dir>
    |-- <product packages>
    |   `--<module names>.py
    `-- doctests                (optional)
        `-- <test names>.txt    (optional)

You can add code that runs the test when the module is invoked as __main__,
but that isn't necessary.

    # Optional - allows tests to run without "-m doctest"
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

    # This version of "main" writes XML test reports
    if __name__ = "__main__":
        import doctest
        import xmlrunner

        suite = doctest.DocTestSuite()
        runner = xmlrunner.XMLTestRunner(output='test-reports')
        runner.run(suite)

Here are the different ways of invoking doctest:

    # Run from the root directory of the python project
    > cd my_dir

    # Run doctests located in a Python module
    # Requires the main logic shown in the snippet
    > python example/calc_func.py

    # Run doctests located in a Python module
    # Does not require the main logic
    > python -m doctest example/calc_funny.py

    # Print verbose output when running doctests
    > python -m doctest -v example/calc_func.py

    # Run doctests located in a seperate text file
    > python -m doctest doctests/test_calc_class.txt

    # Write XML test report using unittest-xml-reporting
    # Requires the appropriate "main" logic
    > python -m example.calc_func

Notes
1) By default, if all tests pass then nothing is printed out.j
2) Doctest expects file paths - not package paths.

## Make your room more advanced, and then use it to rebuild your game yet again but this time, unit test as you go.

Done.