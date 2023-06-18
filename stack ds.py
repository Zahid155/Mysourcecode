def create_stack():
    stack=[]
    return stack

def check_empty(stack):
    return len(stack)==0
    
def push(stack,item):
    stack.append(item)
    print("Pushed item:"+item)

def pop(stack):
 if(check_empty(stack)):
     return "stack is empty"
 return stack.pop()
  
stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
print("\n")
print("Popped item:"+pop(stack))
print("\n")
print("Stack after popping an element" + str(stack))