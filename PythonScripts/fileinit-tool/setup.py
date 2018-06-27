from setuptools import setup

setup(
    name="fileinit",
    packages=["fileinit"],
    entry_points={
        "console_scripts": [
            "fileinit = fileinit.init:main",
        ],
    },
)