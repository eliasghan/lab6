from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")

name = "calculator_Elias_Ghanem"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("name", "calculator_Elias_Ghanem")
    project.set_property("version", "0.1")
    project.set_property("default_task", "publish")
    project.set_property("unittest_module", "tests.unittest")
    # Tests live in tests/unittest and follow the test_*.py naming convention
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Elias_Ghanem")
    project.set_property("unittest_module_glob", "test_*")
