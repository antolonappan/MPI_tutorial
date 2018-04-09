from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a' : 7, 'b' : 3}
else:
    data = None
data = comm.bcast(data, root=0)

if rank != 0:
    print('After broadcasting', data)
