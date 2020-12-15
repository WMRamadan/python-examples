from distutils.core import setup, Extension

module = Extension("pyModule", sources = ["pyModule.c"])

setup(name="PackageName",version="1.0",description="Package for pyModule",ext_modules=[module])
