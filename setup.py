from distutils.core import setup
import setuptools

setup(
   name='myDB', 
   version='0.1dev',
   license='MIT', 
   url="https://github.com/AkashSCIENTIST/myDB",
   package_dir={"":"src"},
   packages = setuptools.find_packages(where="src"),
    python_requires=">=3.6",
   long_description=open('README.md').read(),
)