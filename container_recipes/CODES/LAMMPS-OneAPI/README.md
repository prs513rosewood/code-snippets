# LAMMPS

This directory contains a Docker recipe that builds [LAMMPS](https://lammps.sandia.gov) with the Intel HPC (legacy) compiler suite. The Docker recipe uses a two stage build to minimize the image size. It compiles both the LAMMPS code as well as the Python interface (via lammpslib).

Build the Docker image with:
```bash
docker build -t lammps .
```

# Singularity

The Docker images can be converted into a Singularity image for use on HPC systems. You need to export the image first and then convert it to Singularity.

Convert the image with:
```bash
docker save lammps -o lammps.tar
singularity build lammps.sif docker-archive://lammps.tar
```

## Running the standalone code

To run the standalone code, execute:

```bash
OMP_NUM_THREADS=4 singularity run dftb.sif mdcore-1.0.1
```

If you get an error
```
OMP: Error #179: Function Can't open SHM2 failed:
OMP: System error #2: No such file or directory
```
you need to bind `/run/shm` into the container. Try executing:
```
OMP_NUM_THREADS=4 singularity run --bind /run/shm:/run/shm dftb.sif mdcore-1.0.1
```

## Running the Python interface

The Python interface can run along the same lines:
```bash
OMP_NUM_THREADS=4 singularity run --bind /run/shm:/run/shm dftb.sif python3 my_python_script.py
```
