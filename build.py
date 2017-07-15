from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing", username="anton-matosov", channel="stable")
    
    builder.add(settings={
        "os": "Arduino",
        "os.board": "XYZrobot1280",
        "compiler": "gcc",
        "compiler.version": "4.9",
        "compiler.libcxx": "libstdc++11",
        "arch": "avr"
    }, options={
        "conan-arduino-toolchain:arduino_version": "1.8.3"
    }, env_vars={
        "CC": "gcc"
    }, build_requires={
        "*": ["conan-arduino-toolchain/1.0.0@anton-matosov/stable"]
    })
    builder.run()
