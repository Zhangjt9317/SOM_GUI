import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SOM_GUI-Zhangjt9317", # Replace with your own username
    version="0.0.1",
    author="Jingtian Zhang",
    author_email="jtz9317@gmail.com",
    description="GUI for SOM tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zhangjt9317/SOM_GUI.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)