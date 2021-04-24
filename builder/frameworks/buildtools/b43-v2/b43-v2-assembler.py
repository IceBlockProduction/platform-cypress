from os.path import join
Import('env', "FRAMEWORK_DIR")

print("Configuring b43-v2 assembler...")

env.Append(
    CPPPATH=[
        join(FRAMEWORK_DIR, "buildtools", "b43-v2", "assembler"),
    ],
)