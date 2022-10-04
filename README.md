from: https://lpsa.swarthmore.edu/ZXform/InvZXform/InvZXform.html
# The inverse Z Transform
Given a Z domain function, there are several ways to perform an inverse Z transform: 
- Long Division
- Direct Computation
- Partial Fraction Expansion with Table Lookup 
- Direct Inversion 

The only two of these that we will regularly use are direct computation and fartial expansion 

![LongDivisionExplanation](/Images/LongDivisionExplanation.png)


Dispite that, when the X(z) function has the form: 

$$
\begin{align}
X(z) = \frac{G(Z)}{H(z)} \\
\end{align}
$$

Where G(z) and H(z) is a big polynomial function with order 4 or above unfactorable then the Long Division Method becomes a great tool. 

Therefore I saw the need to create a tool that uses this method to get the first n coefficients of the function in Python. 

