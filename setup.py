import codecs
import subprocess

from setuptools import setup, find_packages

with codecs.open("README.md", encoding="utf-8") as f:
    readme = f.read()


def get_version():
    # this returns something like 'v3.10.0-23-g47040b55' or 'v3.10.0'
    git_release = (
        subprocess.run("git describe --tags", shell=True, capture_output=True)
        .stdout.decode("utf-8")
        .strip()
    )

    # remove the leading 'v' for a proper PEP440 version
    git_release = git_release.replace("v", "")

    # simplify dev versions to PEP440
    if "-" in git_release:
        version = git_release.split("-")[0]
        version = version + ".dev0"
    else:
        version = git_release

    return version


setup(
    name="gitlabform",
    version=get_version(),
    description="🏗 Specialized configuration as a code tool for GitLab projects, groups and more"
    " using hierarchical configuration written in YAML",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://gitlabform.github.io/gitlabform",
    author="Greg Dubicki and Contributors",
    keywords=["cli", "yaml", "gitlab", "configuration-as-code"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE", "version", "*.md", "config.yml"]},
    include_package_data=True,
    python_requires=">=3.8.0",
    install_requires=[
        "certifi==2024.2.2",
        "cli-ui==0.17.2",
        "ez-yaml==1.2.0",
        "Jinja2==3.1.4",
        "luddite==1.0.4",
        "MarkupSafe==2.1.5",
        "mergedeep==1.3.4",
        "packaging==24.0",
        "python-gitlab==4.4.0",
        "requests==2.31.0",
        "ruamel.yaml==0.17.21",
        "types-requests==2.31.0.20240406",
        "yamlpath==3.8.2",
    ],
    extras_require={
        "test": [
            "coverage==7.5.1",
            "cryptography==42.0.7",
            "deepdiff==7.0.1",
            "mypy==1.10.0",
            "mypy-extensions==1.0.0",
            "pre-commit==2.21.0",  # not really for tests, but for development
            "pytest==8.2.0",
            "pytest-cov==5.0.0",
            "pytest-rerunfailures==14.0",
            "xkcdpass==1.19.9",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    entry_points={
        "console_scripts": [
            "gitlabform=gitlabform.run:run",
        ],
    },
)
