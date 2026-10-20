from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "my_python_project"
version = "1.0"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_target", "target")
    project.set_property("dir_source_unittest_python", "src/unittest/python")
    # Pick up test files named test_*.py
    project.set_property("unittest_module_glob", "test_*")

    project.build_depends_on("mock")
    project.build_depends_on("coverage")
