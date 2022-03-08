from setuptools import setup

setup(
   name='international_data_preprocessing',
   version='1.0',
   description='A module to help normalize international data based on population, inflation, and foreign exchange rates',
   author='Emma Carlson',
   author_email='emcar98@uw.edu',
   packages=['international_data_preprocessing'],
   install_requires=['pandas'],
   license='MIT',
   url='https://github.com/emcarlson2017/international-data-preprocessing',
   package_data={'international_data_preprocessing' : ['international_data_preprocessing/data/*.csv']},
   include_package_data=True,
)