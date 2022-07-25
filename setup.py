import setuptools
#import os

#print(os.listdir("."))

long_description = "KVH format reader/writer"
import kvh
version = kvh.__version__

setuptools.setup(
   name="kvh",
   version=version,
   description="KVH format reader/writer",
   keywords="key-value hierarchy",
   license="GNU General Public License v2 or later (GPLv2+)",
   long_description=long_description,
   author="Serguei Sokol",
   author_email="sokol@insa-toulouse.fr",
   url="https://github.com/MathsCell/kvh/",
   packages=setuptools.find_packages(where="."),
   package_data={"kvh": ["*.txt"]},
   py_modules=["kvh"],
   classifiers=[
      "Environment :: Console",
      "Intended Audience :: End Users/Desktop",
      "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
      "Operating System :: OS Independent",
      "Programming Language :: Python :: 3",
      "Topic :: Scientific/Engineering",
      "Topic :: Text Processing",
   ],
   project_urls={
      "Source": "https://github.com/mathscell/kvh",
      "Tracker": "https://github.com/mathscell/kvh/issues",
   },
   python_requires=">=3.6",
)
