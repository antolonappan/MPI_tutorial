from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

no = 100000000
summ = 0

for i in range(rank,no+1,size):
        summ += i
tot = comm.gather(summ,root=0)

if rank==0:
   print(sum(tot))


