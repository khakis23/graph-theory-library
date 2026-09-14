#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "aStar.h"

namespace py = pybind11;


PYBIND11_MODULE(_core, m) {
    m.doc() = "A* Pathfinding Engine";

    // Heuristic enum
    py::enum_<Heuristic>(m, "Heuristic")
        .value("EUCLIDEAN", Heuristic::EUCLIDEAN)
        .value("MANHATTAN", Heuristic::MANHATTAN)
        .value("CHEBYSHEV", Heuristic::CHEBYSHEV)
        .value("NONE", Heuristic::NONE)
        .export_values();

    // Vec2 used in the engine
    py::class_<Vec2>(m, "Vec2")
        .def(py::init<int, int>(), py::arg("x") = 0, py::arg("y") = 0)
        .def_readwrite("x", &Vec2::x)
        .def_readwrite("y", &Vec2::y)
        .def("__repr__", [](const Vec2 &v) {
            return "(" + std::to_string(v.x) + ", " + std::to_string(v.y) + ")";
        })
        .def("__eq__", [](const Vec2 &a, const Vec2 &b) { return a == b; })
        .def("__hash__", [](const Vec2 &v) { return Vec2Hash()(v); });

    // AStar class
    py::class_<AStar>(m, "AStar")
        .def(py::init<char>(), py::arg("predef") = 'a')
        .def(py::init<const std::vector<std::vector<bool>>&>(), py::arg("map"))
        .def("printMap", [](const AStar &self) { self.printMap(); })
        .def("setHeuristic", &AStar::setHeuristic, py::arg("h"))
        .def("setLivePrintSpeed", &AStar::setLivePrintSpeed, py::arg("ms"))
        .def("find", &AStar::find, py::arg("start"), py::arg("end"), py::arg("live_print") = false);

    // Free helper functions
    m.def("clearScreen", &clearScreen);
    m.def("getNeighbors", &getNeighbors, py::arg("pos"));
}

