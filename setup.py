import cx_Freeze

executables = [cx_Freeze.Executable("PingPong.py")]

cx_Freeze.setup(
    name="Ping-Pong!",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["PingPong.jpg"]}},
    executables=executables

    )
