from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        'graphs_tblack3250._core',
        [
            "src/bindings.cpp",
            "AStar/aStar/src/aStar.cpp",
        ],
        include_dirs=["AStar/aStar/include",],
        cxx_std=20,
    ),
]

setup(
    packages=['graphs_tblack3250'],
    package_dir={"": "src"},
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
