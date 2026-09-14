#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "aStar.h"

namespace py = pybind11;


PYBIND11_MODULE(_core, m) {
    m.doc() = "A* Pathfinding Engine";

    // Vec2 used in the engine
    py::class_<Vec2>(m, "Vec2")
        .def(py::init<int, int>(), py::arg("x") = 0, py::arg("y") = 0)
        .def_readwrite("x", &Vec2::x)
        .def_readwrite("y", &Vec2::y);

    // AStar class
    py::class_<AStar>(m, "AStar")
         .def(py::init<char>(), py::arg("predef") = 'a')
        .def(py::init<const std::vector<std::vector<bool>>&>())
        .def("find", &AStar::find, py::arg("start"), py::arg("end"), py::arg("live_print") = false);

    // TODO Dijkstra's (if time permits)
}

