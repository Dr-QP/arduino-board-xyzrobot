from conans import ConanFile
import os

class ArduinoboardxyzrobotConan(ConanFile):
    name = "arduino-board-xyzrobot"
    version = "1.0.0"
    license = "LGPL"
    url = "https://github.com/Dr-QP/arduino-board-xyzrobot"
    description = "XYZrobot board conan package for arduino builds"
    settings = None
    exports_sources = "XYZrobot/*"

    def package(self):
        self.copy("*", dst="XYZrobot", src="XYZrobot", keep_path=True)

    def package_info(self):
        self.env_info.ARDUINO_BOARD_PATH = os.path.join(
            self.package_folder, "XYZrobot")
