from dataclasses import dataclass
from unittest import result
data = {1, 3, 5, 7}

result = {i ** 2 for i in data}
print(result)
    
