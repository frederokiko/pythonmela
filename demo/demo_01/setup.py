from cx_Freeze import setup, Executable

setup(
    name="Puissance",
    version="0.1",
    description="Jeux Application",
    executables=[Executable("puissance4.py")]
)


