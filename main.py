from problem import NQueensProblem
from search import depth_first_search, breadth_first_search, uninformed_graph_search, uninformed_tree_search
from draw_board import draw


if __name__ == '__main__':
    
    print()
    print( '=' * 50)
    print( "NQueensProblem")
    print( '=' * 50)
    
    search = {1: depth_first_search, 
              2: breadth_first_search}
    
    N = int(input("Enter the number of queens:"))
    qp = NQueensProblem(N)
    
    print()
    print("Enter the type of search to use")
    print("1. Depth First Search")
    print("2. Breadth First Search")
    
    searchType = int(input())
    dfts = search[searchType](qp, searchType, search_type=uninformed_tree_search)
    
    print( "Solution", dfts.solution())
    draw('node', 1, 'delay')