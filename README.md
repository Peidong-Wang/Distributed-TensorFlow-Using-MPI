# Distributed-TensorFlow-Using-MPI
Template for Deploying Distributed TensorFlow on Clusters like Ohio Supercomputer Center (OSC) Owens Using MPI

## Brief Description
Scripts in this repository can be used on dynamically allocated clusters like OSC Owens. It combines mpi4py with the typical distributed TensorFlow cluster settings (see the template at https://www.tensorflow.org/deploy/distributed). The basic idea is to use MPI to traverse among the nodes and set up the TensorFlow cluster.

## Contents
1. distributed_tensorflow.sh: the PBS script you can use while submitting jobs
2. cluster_specs.py: get the nodes you acquired for this job and convert this information into the corresponding ps_hosts and worker_hosts in TensorFlow
3. cluster_dispatch.py: specify job_name and task_index and deploy the job
4. example.py: a simple example script for testing. Note that the functions in this example may be depracated soon and you should design your model based on the template at https://www.tensorflow.org/deploy/distributed. Also note that this example script may have a different license from the one for this repository.

## Arguments
Most of the arguments should be modified in distributed_tensorflow.sh. However, you can always change the stdout outputs (the contents in print()) in cluster_dispath.py.
