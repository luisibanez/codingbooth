from setuptools import setup

setup(
  name='Coding Booth',
  version='0.0.1',
  long_description=__doc__,
  packages=['codingbooth'],
  include_package_data=True,
  zip_safe=False,
  install_requires=['Flask >= 0.8']
)
