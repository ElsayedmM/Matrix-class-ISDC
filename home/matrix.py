import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if self.h == 1:
            deter = self[0][0] 
        
        if self.h == 2:
            deter= self[0][0]*self[1][1] - self[0][1]*self[1][0]
        
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        return deter
        # TODO - your code here

    def trace(self):
        trace=0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        l=self.h
      
        for i in range(self.h):
                trace += self[i][i]
        
        return trace
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if self.h == 1:
            inv = 1/self[0][0]
        
        if self.h == 2:
            d = Matrix.determinant(self)
            self.g[0][1]=-self.g[0][1]*(1/d)
            self.g[1][0]=-self.g[1][0]*(1/d)
            s=self.g[0][0]
            sw=self.g[1][1]
            self.g[0][0]=(1/d)*sw
            self.g[1][1]=(1/d)*s

          
        # TODO - your code here
        return self
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        l = self.h
        w = self.w
        T = zeroes(l,w)
        
        for i in range(self.h):
            for j in range(self.w):
                T[j][i]=self[i][j]
        
        return T
    
    def mul(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        l = self.h
        w = other.w
        ans= zeroes(l,w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                        inn= self[i][k] * other[k][j]
                        
                        ans[i][j] = int(ans[i][j]) + inn
        return ans
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
                raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        else:
            #   
            # TODO - your code here
        
            for i in range (self.h):  
                for j in range (self.w):
                    other[i][j] = other[i][j] + self[i][j] 
                 
               
            return other
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        E = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                E[i][j]=-self[i][j]

        return E

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
                raise(ValueError, "Matrices can only be SUBTRACTED if the dimensions are the same") 
        else:
            #   
            # TODO - your code here
        
            for i in range (self.h):  
                for j in range (self.w):
                    other[i][j] = self[i][j] - other[i][j] 
                 

            return other

    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        l = self.h
        w = other.w
        ans= zeroes(l,w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                        inn= self[i][k] * other[k][j]
                        
                        ans[i][j] = int(ans[i][j]) + inn
        return ans
    
    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            pass
        
            for i in range(self.h):
                for j in range(self.w):
                    self[i][j] = self[i][j] *other
                 
        return self