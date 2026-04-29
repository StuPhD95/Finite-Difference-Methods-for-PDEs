# Finite-Difference-Methods-for-PDEs
A collection of finite difference methods for solving two common partial differential equations (PDEs), featuring implementations and comparisons. For **parabolic problems** (e.g. the diffusion equation), the first method considered is an *explicit method*, which uses the below approximations. 
- Forward difference approximation of $\mathcal{O}(h_t)$ for the time derivative

$$\dfrac{\partial u}{\partial t}(x_i,t_{l})\approx \dfrac{u^{l+1}_i-u^l_i}{h_t}, \quad i=1,\ldots,m, \quad  l=0,\ldots,N-1.$$

- Central difference approximation of $\mathcal{O}(h^2_x)$ for the space derivative

$$\dfrac{\partial^2 u}{\partial x^2}(x_i,t_{l})\approx \dfrac{u^{l}_{i-1}-2u^{l}_i+u^{l}_{i+1}}{h^2_x}, \quad i=1,\ldots,m, \quad  l=0,\ldots,N-1.$$

The second method is an *implicit method*, which uses the below approximations. 
- Backward difference approximation of $\mathcal{O}(h_t)$ for the time derivative

$$\dfrac{\partial u}{\partial t}(x_i,t_{l+1})\approx \dfrac{u^{l+1}_i-u^l_i}{h_t}, \quad i=1,\ldots,m, \quad  l=0,\ldots,N-1.$$

- Central difference approximation of $\mathcal{O}(h^2_x)$ for the space derivative

$$\dfrac{\partial^2 u}{\partial x^2}(x_i,t_{l+1})\approx \dfrac{u^{l+1}_{i-1}-2u^{l+1}_i+u^{l+1}_{i+1}}{h^2_x}, \quad i=1,\ldots,m, \quad  l=0,\ldots,N-1.$$

The third and final method is the *Crank-Nicolson method*, which takes an average of the two previous methods. This method is of order $\mathcal{O}(h^2_t)$ and $\mathcal{O}(h^2_x)$. Like the implicit method, it is unconditionally stable. The explicit method is stable if and only if $s\le 0.5$ where 

$$s=\frac{D h_t}{h^2_x},$$

for $D>0$. In the case of the diffusion equation, $D$ represents the diffusion coefficient. For **hyperbolic problems** (e.g. the wave equation), an **explicit method** is used with the below approximations.

- Central difference approximation of $\mathcal{O}(h^2_t)$ for the time derivative

$$\dfrac{\partial^2 u}{\partial t^2}(x_i,t_{l})\approx \dfrac{u^{l-1}_{i}-2u^{l}_i+u^{l+1}_{i}}{h^2_t}, \quad i=1,\ldots,m, \quad  l=0,\ldots,N-1.$$

- Central difference approximation of $\mathcal{O}(h^2_x)$ for the space derivative

$$\dfrac{\partial^2 u}{\partial x^2}(x_i,t_{l})\approx \dfrac{u^{l}_{i-1}-2u^{l}_i+u^{l}_{i+1}}{h^2_x}, \quad i=1,\ldots,m, \quad  l=0,\ldots,N-1.$$

This method is stable if and only if $s\le 1$ where

$$s=\frac{c^2 h^2_t}{h^2_x},$$

for $c>0$. In the case of the wave equation, $c$ represents the wave speed.

**One-Dimensional Diffusion Equation** 

![Diffusion_Equation](Figures/Diffusion_Implicit_Method.png)

![Diffusion_Equation](Figures/Diffusion_CN.png)



**One-Dimensional Wave Equation** 
