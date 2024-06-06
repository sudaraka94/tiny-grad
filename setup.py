import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tinygrad",
    version="0.1.0",
    author="Sudaraka Jayathilaka",
    author_email="sudarakayasindu@gmail.com",
    description="A tiny scalar valued autograd engine with neural net library build using vanilla python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudaraka94/tinygrad",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
