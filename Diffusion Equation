# The one-dimensional diffusion equation is solved using three different numerical schemes.
# Require s <= 0.5 for stability of the explicit method. While the explicit and Crank-Nicolson
# methods are unconditionally stable, the data value at u(0,0) (being both 20 and 100) is only
# used for the latter.  

from numpy import linspace, ones, zeros, vstack, hstack
from numpy import meshgrid, sin, pi, copy
from scipy.sparse import spdiags, eye
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt 

D = 0.008                # diffusion coefficient
a = 0                    # space domain [a, b]
b = 2
T = 200                   # time domain [0, T]

m = 39                    # m+1 subintervals in x
N = 20                    # N subintervals in t
x = linspace(a, b, m+2);  # m interior nodes + 2 end points
t = linspace(0, T, N+1);  # 1 initial time + N further times (open)
hx = (b-a)/(m+1)
ht = T/N
s = D * ht / hx**2       # stability constant

# initialize
U = zeros((m+2, N+1))
U[:,0]   = 20 #20 + 80*sin(pi*(x-a)/(b-a)) # initial  condition at t = 0
U[0,:]   = 100 #20                          # boundary condition at x = a
U[m+1,:] = 20                          # boundary condition at x = b
print('U =\n', U)

# three methods
method = 1; # Method 1: explicit method (FTCS)
#method = 2; # Method 2: implicit method (BTCS)
#method = 3; # Method 3: Crank-Nicolson method  

if method == 1: # Method 1: explicit method (FTCS)
    om2s = 1-2*s
    for ell in range(N):
        U[1:m+1, ell+1] = \
            s*U[0:m, ell] + om2s*U[1:m+1, ell] + s*U[2:m+2, ell]

elif method == 2: # Method 2: implicit method (BTCS)
    e = ones(m)
    A = spdiags(vstack((-s*e, (1+2*s)*e, -s*e)), [-1, 0, 1], m, m)  
                                        # tridiagonal matrix A
    print('A =\n', A.toarray())         # A in dense format
    for ell in range(N):
        r = copy(U[1:m+1, ell])         # must copy 
        r[0]   += s*U[0,   ell+1]
        r[m-1] += s*U[m+1, ell+1]
        U[1:m+1, ell+1] = spsolve(A, r) # Thomas algorithm O(m)
          
else: # Method 3: Crank-Nicolson method  
    e = ones(m)
    A = spdiags(vstack((-(s/2)*e, (1+s)*e, -(s/2)*e)), [-1, 0, 1], m, m) 
                                        # tridiagonal matrix A
    print('A =\n', A.toarray())         # A in dense format
    so2 = s/2
    oms = 1-s
    for ell in range(N):
        r = so2*U[0:m, ell] + oms*U[1:m+1, ell] + so2*U[2:m+2, ell]
        r[0]   += so2*U[0,   ell+1]
        r[m-1] += so2*U[m+1, ell+1]
        U[1:m+1, ell+1] = spsolve(A, r) # Thomas algorithm O(m)
 
print('U =\n', U)

print('stability constant =', s )

# plot solution
X, Y = meshgrid(x, t)
fig = plt.figure(2)
ax = fig.add_subplot(projection='3d')
surf = ax.plot_wireframe(X, Y, U.T)     

ax.set_xlabel('x'); ax.set_ylabel('t'); ax.set_zlabel('u')
plt.title("1D diffusion equation")
plt.show()
