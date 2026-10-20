# my_python_project

A small Python project built with PyBuilder, with a Makefile that runs the common build steps.

## Build process

`build.py` describes the project to PyBuilder: name, version, where the source (`src/main/python`)
and unit tests (`src/unittest/python`) are, the output folder (`target`), and the build-time
dependencies (`mock`, `coverage`). PyBuilder goes through its tasks in order: prepare,
compile_sources, run_unit_tests, package. It writes reports and the packaged distribution to `target/`.

## Makefile targets

| Target         | Command                           | Purpose                                             |
|----------------|-----------------------------------|-----------------------------------------------------|
| `clean`        | `pyb clean`                       | Deletes `target/` so the next build starts clean    |
| `install_deps` | `pip install -r requirements.txt` | Installs the project's dependencies                 |
| `test`         | `pyb run_unit_tests`              | Runs the unit test suite                            |
| `build`        | `pyb package`                     | Runs the tests, then packages the project           |
| `all`          | all of the above, in order        | One command for the whole pipeline                  |

`.PHONY` tells `make` that these names are commands, not files, so they always run.

## Why use a Makefile

- You type one short command (`make test`) instead of remembering the long ones.
- Every developer and the CI server run the same steps the same way.
- Targets can be chained (`all`), so a full clean build needs a single command.
- The Makefile documents how the project is built.

## Running

```
make all          # or: mingw32-make all  (Windows)
```
