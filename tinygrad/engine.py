class Value:
    """
    Wraps a scaler value and provides an interface.
    """

    def __init__(self, data, prev=None, label=""):
        self.grad = 0.0
        self.data = data
        self._prev = prev
        self._backward = lambda : None
        self._label = label

    def __repr__(self) -> str:
        return f"data: {self.data}, grad: {self.grad}"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other) # wrap other with Value if it is not already one
        out = Value(self.data + other.data, prev=(self, other), label="+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data*other.data, prev=(self, other), label="*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        
        out._backward = _backward
        return out

    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        other = other if isinstance(other, Value) else Value(other) 
        return self * other ** -1
    
    def __rtruediv__(self, other):
        return other * self ** -1
    
    def __pow__(self, power):
        assert isinstance(power, (int, float)) # only supports floats and int as a power (doesn't support Value as a power)
        out = Value(self.data**power, prev=(self,), label="**")

        def _backward():
            self.grad += power * (self.data**(power-1)) * out.grad
            
        out._backward = _backward
        return out
