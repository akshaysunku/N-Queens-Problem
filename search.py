from draw_board import draw

def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

def todo():
    raise NotImplementedError('You must complete the implementation.')

#______________________________________________________________________________
# Queues: FIFOQueue, LIFOQueue

class Queue:
    """Queue is an abstract class/interface. There are three types:        
        FIFOQueue(): A First In First Out Queue.
        LIFOQueue(): A Last In First Out Queue.
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue        
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    """
   
    def append(self, item):
        abstract()
    
    def pop(self):
        abstract()


class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []
    
    def append(self, item):
        """Add to the end"""
        self.A.append(item)

    def pop(self):
        """Remove the first item"""
        return self.A.pop(0)
        
    def __contains__(self, item):
        return item in self.A
    
    def __len__(self):
        return len(self.A)
    
    def __repr__(self):
        """Return [A[0], A[1], ...]"""
        rep = "[" + str(self.A[0])
        for i in range(1, len(self.A)):
            rep += ", " + str(self.A[i])
        rep += "]"
        return rep


class LIFOQueue(Queue):
    """A Last-In-First-Out Queue."""
    def __init__(self):
        self.A = []
    
    def append(self, item):
        """Add to the end"""
        self.A.append(item)

    def pop(self):
        """Remove the last item"""
        return self.A.pop()
        
    def __contains__(self, item):
        return item in self.A
    
    def __len__(self):
        return len(self.A)
    
    def __repr__(self):
        """Return [A[0], A[1], ...]"""
        rep = "[" + str(self.A[0])
        for i in range(1, len(self.A)):
            rep += ", " + str(self.A[i])
        rep += "]"
        return rep


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."

        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost

        self.depth=0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem, searchType):
        "List the nodes reachable in one step from this node."
        return [self.child_node(problem, action)
                for action in problem.actions(self.state, searchType)]

    def child_node(self, problem, action):
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action,
                    problem.path_cost(self.path_cost, self.state, action, next_node))

    def solution(self):
        "Return the sequence of actions to go from the root to this node."
        return [node.action for node in self.path()[1:]]

    def path(self):
        "Return a list of nodes forming the path from the root to this node."
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


# Uninformed Search

def uninformed_tree_search(problem, searchType, frontier):
    """Uninformed tree search. Frontier is either a
    FIFOQueue or a LIFOQueue.
    """
    delay = int(input("Enter the delay time in milliseconds:"))
    frontier.append(Node(problem.initial))
    while frontier: 
        print( "Frontier: ", str(frontier))
        node = frontier.pop()
        print( "\nNode: ", str(node))
        print()
        draw(node, 0, delay)
    
        if problem.goal_test(node.state):
            return node
        for child in node.expand(problem, searchType):           
            frontier.append(child)

    return None
            
            
def uninformed_graph_search(problem, searchType, frontier):
    """Uninformed graph search. Frontier is either a
    FIFOQueue or a LIFOQueue.
    Because it is uninformed, it does not check whether
    a better path to a Node in frontier is found.
    """
    delay = int(input("Enter the delay time in milliseconds:"))
    frontier.append(Node(problem.initial))
    explored = []
    while frontier:
        print( "Frontier: ", str(frontier))
        node = frontier.pop()
        print( "\nNode: ", str(node))
        print()
        draw(node, 0, delay)
        
        if problem.goal_test(node.state):
            return node
        explored.append(node.state)
        for child in node.expand(problem, searchType):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
    return None

def breadth_first_search(problem, searchType, search_type=uninformed_tree_search):
    return search_type(problem, searchType, FIFOQueue())

def depth_first_search(problem, searchType, search_type=uninformed_tree_search):
    return search_type(problem, searchType, LIFOQueue())
