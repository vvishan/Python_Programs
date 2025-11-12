class model_config:
    def __init__(self,lr):
        self.lr = lr
        
    @property
    def lr(self):
        return self._lr
    
    @lr.setter
    def lr(self,value):
        if value <= 0:
            raise ValueError("learning rate must be positive")
        self._lr = value


cf = model_config(0.041)
cf.lr = 0.05
print(cf.lr)

# when to use @ prority + when to want attribute like access (obj:x),but need logic behind the scene


