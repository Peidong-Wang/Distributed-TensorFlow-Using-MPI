from mpi4py import MPI
import socket
import os
import argparse

FLAGS=None


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    ps_hosts_list = FLAGS.ps_hosts.split(',')
    worker_hosts_list = FLAGS.worker_hosts.split(',')
    num_ps_hosts = len(ps_hosts_list)
    num_worker_hosts = len(worker_hosts_list)
    num_hosts = num_ps_hosts + num_worker_hosts

    for rank_rotate in range(num_hosts):
        if rank == rank_rotate:
            print("I am rank " + str(rank_rotate) + "...")
            hostname = socket.gethostname()
            print("My hostname is: " + hostname)
            for ps_hosts_rotate in range(num_ps_hosts):
                if hostname == ps_hosts_list[ps_hosts_rotate].split(':')[0]:
                    print("My job ID is: ps" + str(ps_hosts_rotate))
                    os.system("python -u " + FLAGS.script + " --ps_hosts=" + FLAGS.ps_hosts + " --worker_hosts=" + FLAGS.worker_hosts + " --job_name=ps --task_index=" + str(ps_hosts_rotate))
            for worker_hosts_rotate in range(num_worker_hosts):
                if hostname == worker_hosts_list[worker_hosts_rotate].split(':')[0]:
                    print("My job ID is: worker" + str(worker_hosts_rotate))
                    os.system("python -u " + FLAGS.script + " --ps_hosts=" + FLAGS.ps_hosts + " --worker_hosts=" + FLAGS.worker_hosts + " --job_name=worker --task_index=" + str(worker_hosts_rotate))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "--ps_hosts",
        type=str,
        default="",
        help="Comma-separated list of hostname:port pairs"
        )
    parser.add_argument(
        "--worker_hosts",
        type=str,
        default="",
        help="Comma-separated list of hostname:port pairs"
        )
    parser.add_argument(
        "--script",
        type=str,
        default="",
        help="The .py file you want to execute"
        )

    FLAGS, unparsed = parser.parse_known_args()
    main()
