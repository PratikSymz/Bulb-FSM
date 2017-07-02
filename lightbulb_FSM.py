from random import randint
from time import clock

## STATE SECTION -------------------------------------------------------------

# Used To Create a STATE BASE CLASS
State = type("State", (object,), {})

class LightOn(State):
    def Execute(self):
        print "Light is ON!"

class LightOff(State):
    def Execute(self):
        print "Light is OFF!"


## TRANSITION SECTION -------------------------------------------------------------

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print "Transitioning......."


## FINITE STATE MACHINE -------------------------------------------------------------

class SimpleFSM(object):
    def __init__(self, char):
        self.char = char                # Stores Current Character / Input Character
        self.states = {}                # Creating a Dictionary for States
        self.transitions = {}           # Creating a Dictionary for Transitions
        self.curState = None            # Stores Current State
        self.trans = None               # Stores Current Transition

    def setState(self, stateName):
        self.curState = self.states[stateName]          # Looks for the current state in the "state" Dictionary by passing in the state name

    def Transition(self, transName):
        self.trans = self.transitions[transName]         # Looks for the current transition in the "transition" Dictionary by passing in the transition name

    def Execute(self):
        if (self.trans):
            self.trans.Execute()
            self.setState(self.trans.toState)
            self.trans = None
            
        self.curState.Execute()


## CHARACTER CLASS -------------------------------------------------------------

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True

## PROGRAM RUN  -------------------------------------------------------------

if ( __name__ == "__main__"):
    light = Char()

    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["toOn"] = Transition("On")        # "On" in Transition matches the "On" in states
    light.FSM.transitions["toOff"] = Transition("Off")

    light.FSM.setState("On")


## MAIN PROGRAM  -------------------------------------------------------------

for i in range(20):
    startTime = clock()         # Records the Current Time
    timeInterval = 1            # Time Limit

    while((startTime + timeInterval) > clock()):            # Loops if the Current Time hasn't passed 1 Second
        pass

    # Clock has passed 1 Second
    if(randint(0,2)):                                       # Skips to Execute if 0, else Executes the whole block (if 1)
        if(light.LightOn):
            light.FSM.Transition("toOff")
            light.LightOn = False

        else:
            light.FSM.Transition("toOn")
            light.LightOn = True

    light.FSM.Execute()
