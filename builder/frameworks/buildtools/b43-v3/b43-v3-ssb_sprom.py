from os.path import join
Import('env', "FRAMEWORK_DIR")

print("Configuring b43-v3 ssb_sprom...")

env.Append(
    CPPPATH=[
        join(FRAMEWORK_DIR, "buildtools", "b43-v3", "ssb_sprom"),
    ],
)