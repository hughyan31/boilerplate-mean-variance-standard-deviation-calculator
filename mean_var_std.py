import numpy as np

def calculate(list):
  
  if len(list)==9:
    n = np.array(list)
    shape = (3,3)
    mat = n.reshape(shape)
    meanvalues =[[np.mean(mat[:,0]),np.mean(mat[:,1]),np.mean(mat[:,2])],[np.mean(mat[0,:]),np.mean(mat[1,:]),np.mean(mat[2,:])],np.mean(mat)]
    varvalues =[[np.var(mat[:,0]),np.var(mat[:,1]),np.var(mat[:,2])],[np.var(mat[0,:]),np.var(mat[1,:]),np.var(mat[2,:])],np.var(mat)]
    stdvalues =[[np.std(mat[:,0]),np.std(mat[:,1]),np.std(mat[:,2])],[np.std(mat[0,:]),np.std(mat[1,:]),np.std(mat[2,:])],np.std(mat)]
    maxvalues =[[np.max(mat[:,0]),np.max(mat[:,1]),np.max(mat[:,2])],[np.max(mat[0,:]),np.max(mat[1,:]),np.max(mat[2,:])],np.max(mat)]
    minvalues =[[np.min(mat[:,0]),np.min(mat[:,1]),np.min(mat[:,2])],[np.min(mat[0,:]),np.min(mat[1,:]),np.min(mat[2,:])],np.min(mat)]
    sumvalues =[[np.sum(mat[:,0]),np.sum(mat[:,1]),np.sum(mat[:,2])],[np.sum(mat[0,:]),np.sum(mat[1,:]),np.sum(mat[2,:])],np.sum(mat)]
    calculations = "{{'mean': {}, 'variance': {}, 'standard deviation': {}, 'max': {}, 'min': {}, 'sum': {}}}".format(meanvalues, varvalues, stdvalues, maxvalues, minvalues, sumvalues)

  else:
    raise ValueError('List must contain nine numbers.')
    
  return calculations