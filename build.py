from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing", username="anton-matosov", channel="stable")
    # builder.add_common_builds()
    builder.add(settings={
        "os": "Arduino",
        "os.board": "XYZrobot1280",
        "compiler": "gcc",
        "compiler.version": "4.9",
        "compiler.libcxx": "libstdc++11",
        "arch": "avr"
    }, env_vars={
        "CC": "gcc"
    })
    builder.run()
