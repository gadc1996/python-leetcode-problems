
from src.p931 import Solution

solution = Solution()

def test_one():
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    assert solution.minFallingPathSum(matrix) == 13

def test_two():
    matrix = [[-19,57],[-40,-5]]
    assert solution.minFallingPathSum(matrix) == -59
    
def test_three():
    matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]
    assert solution.minFallingPathSum(matrix) == -36

def test_available_paths_one():
    matrix_depth = 1
    expected = ["0"]
    
    assert sorted(solution.paths(matrix_depth))  == sorted(expected)
       
def test_available_paths_two():
    matrix_depth = 2
    expected = [
        "00", 
        "01", 
        "10", 
        "11", 
    ]
    assert sorted(solution.paths(matrix_depth))  == sorted(expected)

def test_available_paths_three():
    matrix_depth = 3
    expected = sorted([
        "000",
        "001",
        "010",
        "011",
        "012",
        "100",
        "101",
        "110",
        "111",
        "112",
        "121",
        "122",
        "210",
        "211",
        "212",
        "221",
        "222",
    ])
    
    actual = sorted(solution.paths(matrix_depth))
    assert actual == expected
