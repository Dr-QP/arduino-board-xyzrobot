#!/usr/bin/env python3

from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy
import os

if __name__ == "__main__":
    builder = ConanMultiPackager(build_policy="outdated")

    builder.add(settings={
        "os": "Arduino",
        "os.board": "XYZrobot1280",
        "compiler": "gcc",
        "compiler.version": "7.3",
        "compiler.libcxx": "libstdc++11",
        "arch": "avr"
    }, build_requires={
        "*": [
            "arduino-sdk/1.8.11@conan/testing",
            "arduino-cmake/1.0.0@conan/testing",
            "cmake_installer/3.16.3@conan/stable"
        ]
    })

    builder.run()
