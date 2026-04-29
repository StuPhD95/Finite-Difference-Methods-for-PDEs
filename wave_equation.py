from numpy import linspace, ones, zeros, vstack, hstack, newaxis
from numpy import meshgrid, sin, pi
import matplotlib.pyplot as plt 

c = 2                    # wave speed
a = 0                    # space domain [a, b]
b = 1      
T = 1                    # time domain [0, T]

m = 39                   # m+1 subintervals in x
N = 80                   # N subintervals in t    
x = linspace(a, b, m+2)  # m interior nodes + 2 end points
t = linspace(0, T, N+1)  # 1 initial time + N further times (open)
hx = (b-a)/(m+1);           
ht = T/N;
s = c**2 * ht**2 / hx**2 # stability constant

# initialize
U = zeros((m+2, N+1))
#U[:,0]   = sin(pi*x) + sin(2*pi*x) # optional initial  condition at t = 0  
#U[:,0]   = x*(x<=0.6) + 1.5*(1-x)*(x>0.6) # optional initial  condition at t = 0 
U[:,0]   = sin(pi*x) # initial  condition at t = 0  
U[0,:]   = 0                        # boundary condition at x = a
U[m+1,:] = 0                        # boundary condition at x = b
#U[m+1,:] = t                       # optional boundary condition at x = b  
print('U =\n', U)

#dUdt = zeros((m+2, 1)) # optional initial derivative condition at t = 0
dUdt = 2*pi*sin(pi*x[:,newaxis])  # initial derivative condition at t = 0  

# explicit method (CTCS)
U[1:m+1, 1] = (s/2)*U[0:m, 0] + (1-s)*U[1:m+1, 0] \
              + (s/2)*U[2:m+2, 0] + ht * dUdt[1:m+1,0]
t1ms = 2*(1-s)
for ell in range(1,N):
    U[1:m+1, ell+1] = s*U[0:m, ell] + t1ms*U[1:m+1, ell] \
                      + s*U[2:m+2, ell] - U[1:m+1, ell-1]
print('U =\n', U)

print('stability constant =', s )

# plot solution
X, Y = meshgrid(x, t)
fig = plt.figure(3)
ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(X, Y, U.T)     
ax.set_xlabel('x'); ax.set_ylabel('t'); ax.set_zlabel('u')
plt.title("1D wave equation")
plt.show()
