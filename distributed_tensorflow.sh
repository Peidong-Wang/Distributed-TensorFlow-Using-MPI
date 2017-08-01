#PBS -N distributed_tensorflow
#PBS -l walltime=01:00:00
#PBS -l nodes=3:ppn=28:gpus=1

export PS_HOSTS=$(python /<path_to_cluster_specs>/cluster_specs.py --hosts_file=$PBS_NODEFILE --num_ps_hosts=1 | cut -f1 -d ' ')
export WORKER_HOSTS=$(python /<path_to_cluster_specs>/cluster_specs.py --hosts_file=$PBS_NODEFILE --num_ps_hosts=1 | cut -f2 -d ' ')

mpiexec -ppn 1 python -u /<path_to_cluster_dispatch>/cluster_dispatch.py --ps_hosts=$PS_HOSTS --worker_hosts=$WORKER_HOSTS \
		--script=/<path_to_your_script>/example.py
