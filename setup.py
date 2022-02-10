import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="mbed-vscode-tools",
    version="0.0.1",
    install_requires=["mbed-tools"],
    entry_points={
        "console_scripts": [
            "mbed-vscode-tools=mbed_vscode_tools.mbed_vscode_tools:main"]
    },
    author="Keisuke Sugiura",
    author_email="std.experimental.optional@gmail.com",
    description="A command-line to facilitate vscode intellisense  for mbed-os.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sterngerlach/mbed-vscode-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires=">=3.7")
