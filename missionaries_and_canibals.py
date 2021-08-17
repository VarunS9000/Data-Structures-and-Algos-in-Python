
class State:
   def __init__(self,leftM,leftC,rightM,rightC,boat):
      self.leftM=leftM
      self.leftC=leftC
      self.rightM=rightM
      self.rightC=rightC
      self.boat=boat
      self.parent=None

def validity(state):
   if(state.leftM>=0 and state.rightM>=0 and state.leftC>=0 and state.rightC>=0 and(state.leftM==0 or state.leftM>=state.leftC)and(state.rightM==0 or state.rightM>=state.rightC)):
      return True
   else:
      return False
   
def leftToRight(state,canibals,missionaries):
   return State(state.leftM-missionaries,state.leftC-canibals,state.rightM+missionaries,state.rightC+canibals,1)

def rightToLeft(state,canibals,missionaries):
   return State(state.leftM+missionaries,state.leftC+canibals,state.rightM-missionaries,state.rightC-canibals,0)
   
   

startState=State(3,3,0,0,0)

def statePossibilities(currentState):
   children=[]
   if(currentState.boat==0):
         if(validity(leftToRight(currentState,2,0))):
            newState=leftToRight(currentState,2,0)
            newState.parent=currentState
            children.append(newState)
           

         if(validity(leftToRight(currentState,0,2))):
             newState=leftToRight(currentState,0,2)
             newState.parent=currentState
             children.append(newState)

         if(validity(leftToRight(currentState,1,1))):
            newState=leftToRight(currentState,1,1)
            newState.parent=currentState
            children.append(newState)

         if(validity(leftToRight(currentState,0,1))):
            newState=leftToRight(currentState,0,1)
            newState.parent=currentState
            children.append(newState)

         if(validity(leftToRight(currentState,1,0))):
            newState=leftToRight(currentState,1,0)
            newState.parent=currentState
            children.append(newState)

   elif(currentState.boat==1):
         if(validity(rightToLeft(currentState,2,0))):
            newState=rightToLeft(currentState,2,0)
            newState.parent=currentState
            children.append(newState)
           

         if(validity(rightToLeft(currentState,0,2))):
             newState=rightToLeft(currentState,0,2)
             newState.parent=currentState
             children.append(newState)

         if(validity(rightToLeft(currentState,1,1))):
            newState=rightToLeft(currentState,1,1)
            newState.parent=currentState
            children.append(newState)

         if(validity(rightToLeft(currentState,0,1))):
            newState=rightToLeft(currentState,0,1)
            newState.parent=currentState
            children.append(newState)

         if(validity(rightToLeft(currentState,1,0))):
            newState=rightToLeft(currentState,1,0)
            newState.parent=currentState
            children.append(newState)

   

   return children
         

   


def bfs():
   stack=list()
   seen=set()
   stack.append(startState)
   while stack:
      currState=stack.pop(0)
      if currState.leftM==0 and currState.leftC==0 and currState.rightM==3 and currState.rightC==3 and currState.boat==1:
         return currState
      else:
         seen.add(currState)
         subStates=statePossibilities(currState)
         for sub in subStates:
            if (sub not in stack) or (sub not in seen):
               stack.append(sub)

   
   return None

   
         
      
    
def finalSolution(state):
   nowState=state
   finalPath=[]
   while nowState.parent is not None:
      finalPath.append(nowState)
      nowState=nowState.parent

   

   return list([(x.leftC,x.leftM,x.rightC,x.rightM,x.boat) for x in finalPath])
      
   
finalState=bfs()
print(finalSolution(finalState))




      
         
   
   

