#include <pybind11/pybind11.h>
#include "NAOKinematics.h"
#include "KMat.hpp"

namespace py = pybind11;

PYBIND11_MODULE(libNaokinematics, m) {
    m.doc() = "NAOKinematics Python bindings";

    py::class_<NAOKinematics>(m, "NAOKinematics")
        .def(py::init<>())
        .def("getForwardEffector", &NAOKinematics::getForwardEffector)
        .def("inverseRightHand", [](NAOKinematics &self, NAOKinematics::kmatTable targetPoint) {
            return self.inverseRightHand(targetPoint);
        })
        .def("inverseLeftHand",[](NAOKinematics &self, NAOKinematics::kmatTable targetPoint) {
            return self.inverseRightHand(targetPoint);
        });
}