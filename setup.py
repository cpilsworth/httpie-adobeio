from setuptools import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = (convert_deps_to_pip(pfile["packages"], r=False),)
test_requirements = convert_deps_to_pip(pfile["dev-packages"], r=False)

version = "0.0.2"

setup(
    name="httpie-adobeio",
    description="AdobeIO plugin for HTTPie.",
    long_description=open("README.rst").read().strip(),
    long_description_content_type="text/x-rst",
    version=f"{version}",
    author="Chris Pilsworth",
    author_email="cpilsworth@gmail.com",
    license="Apache License 2.0",
    url="https://github.com/cpilsworth/httpie-adobeio",
    download_url=f"https://github.com/cpilsworth/httpie-adobeio/releases/download/release-{version}/httpie-adobeio-{version}.tar.gz",
    py_modules=["httpie_adobeio"],
    zip_safe=False,
    entry_points={
        "httpie.plugins.auth.v1": ["httpie_adobeio = httpie_adobeio:AdobeIOAuthPlugin"]
    },
    install_requires=requirements,
    tests_require=test_requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Environment :: Plugins",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
