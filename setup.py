from setuptools import setup, find_packages

version = '0.1'

setup(name='ec2_scheduler',
      version=version,
      description="Schedule stop & start of ec2 instances",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ec2 cost optimization',
      author='Padmakar Ojha',
      author_email='padmakarojha@snapdeal.com',
      url='',
      license='GPL-3.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["boto","click","croniter"],
      entry_points={
          'console_scripts': [
              'ec2_scheduler = ec2_scheduler.main:main',
          ]
      }      
)
