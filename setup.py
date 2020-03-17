#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import versioneer

__author__     = "Lars Pastewka, Johannes Hörmann"
__copyright__  = "Copyright 2020, IMTEK Simulation, University of Freiburg"
__maintainer__ = "IMTEK Simulation"
__email__      = "johannes.hoermann@imtek.uni-freiburg.de"
__date__       = "Mar 17, 2020"

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='imtek-simulation-code-snippets',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description='This repository contains a random collection of code snippets for pre- and postprocessing simulation runs with Ovito, ASE and other tools.',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        url='https://github.com/IMTEK-Simulation/code-snippets',
        author='Lars Pastewka, Johannes Hörmann',
        author_email='johannes.hoermann@imtek.uni-freiburg.de',
        license='MIT',
        packages=find_packages(),
        package_data={'': ['ChangeLog.md']},
        python_requires='>3.6.8',
        zip_safe=False,
        install_requires=[
            'numpy>=1.16.2',
            'scipy>=1.2.1',
            'pandas>=0.24.2',
        ],
        extras_require={
            "GMX":  [
                "ParmEd>=3.1.0",
                "GromacsWrapper>=0.8.0",
            ],
            "MPI": [
                "mpi4py>=3.0.1",
            ],
            "NetCDF": [
                "netCDF4>=1.5.1.2",
            ],
            "Ovito": [
                "ovito", # not sure how to specify dependency on Ovito
            ],
        },
        entry_points={
            'console_scripts': [
                'extend_ndx_by_per_atom_groups = GROMACS-data.extend_ndx_by_per_atom_groups:main [GMX]',
            ],
        },
    )