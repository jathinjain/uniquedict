import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uniquedict",
    version="0.0.1",
    author="Jathin R",
    author_email="jatinrathod1307@gmail.com",
    description="This is a simple package which let user to initially store all the unique values of training data in the form of the dictionary",
    url="https://github.com/jathinjain/unique_dict.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)