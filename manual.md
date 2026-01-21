### Modular

#### Input

#### Interpret
Interpret from **pair** in scheme (a string class     when input in python) to **LinkList** in python.

Also, nil should be defined.

#### Evaluate and Apply

Two function will be defined, **eval** and **apply**. 
   
   - The **eval** function gets a expression (expr, a LinkList-type) and the current frame (env). It evaluates the expression directly, if the expression is **self-evaluating** (like 1, a); or recursively call **apply** and **eval**, if the expression is compound.
   - The **apply** function gets a procedure (procedure), several arguments (a LinkList-type args) and the current environment (env). It apply the procedure to arguments, and if certain arguments are expression, it will call **eval** function to evaluate them.
  
#### Procedure



#### Output


### classes
- Procedure (alias)
- LinkList
  ```python
  class LinkList:
      def __init__(self, first, rest):
          self.first = first
          self.rest = rest
    ```
- Frame
  ```python
  class Frame:
    def __init__(self, father_frame):
        self.father = father_frame
        self.bonuds = {}
    def bound(name, value):
        self.bounds["name"] = value
  ```