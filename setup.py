import setuptools

setuptools.setup(
    name="pyfx",
    version="0.0.1",
    entry_points={
        "console_scripts": ["pyfx=pyfx.cli:main"]
    }
)
