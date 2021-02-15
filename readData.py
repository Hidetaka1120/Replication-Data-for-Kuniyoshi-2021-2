import numpy as np

def readFile(file):
    # This is where the reading of the binary file is taken care of

    #Contains a list of all the fields-files
	with open(file,'r') as f:
	    _,_,_=np.fromfile(f,dtype=np.int32,count=3)
	    time=np.fromfile(f,dtype=np.float32,count=1)[0]
	    nx,ny,nz=np.fromfile(f,dtype=np.int32,count=3)
	    xmax=np.fromfile(f,dtype=np.float32,count=1)[0]
	    ymax=np.fromfile(f,dtype=np.float32,count=1)[0]
	    ssz=np.fromfile(f,dtype=np.float32,count=nz)
	    eta=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    wid=np.fromfile(f,dtype=np.float32,count=1)[0]
	    rho=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    vx=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    vy=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    vz=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    bx=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    by=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    bz=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    u=np.reshape(np.fromfile(f,dtype=np.float32,count=nx*ny*nz),(nz,ny,nx))
	    _=np.fromfile(f,dtype=np.float32,count=1)[0]
	    gamma=np.fromfile(f,dtype=np.float32,count=1)[0]
	    _=np.reshape(np.fromfile(f,dtype=np.float32,count=ny*nz),(nz,ny))

	z=ssz
	hh=np.linspace(0,nx-1,nx)
	hh=(hh-1.)*xmax/float(nx-3)
	x=hh
	hh=np.linspace(0,ny-1,ny)
	hh=-ymax+2.*ymax/float(ny-3)*(hh-1.)
	y=hh

	eta*=wid

	varDictionary = {}
	varDictionary.update({"time":time})
	varDictionary.update({"nx":nx})
	varDictionary.update({"ny":ny})
	varDictionary.update({"nz":nz})
	varDictionary.update({"x":x})
	varDictionary.update({"y":y})
	varDictionary.update({"z":z})
	varDictionary.update({"eta":eta})
	varDictionary.update({"ro":rho})
	varDictionary.update({"vx":vx})
	varDictionary.update({"vy":vy})
	varDictionary.update({"vz":vz})
	varDictionary.update({"bx":bx})
	varDictionary.update({"by":by})
	varDictionary.update({"bz":bz})
	varDictionary.update({"pr":u})
	varDictionary.update({"gamma":gamma})

	return varDictionary