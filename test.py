from main import invert_matrix

def test_invert_matrix():
    assert invert_matrix([[2, 0],[0,2]], 5) == [[3, 0],[0,3]]
    assert invert_matrix([[2, 0],[0,2]], 3) == [[2, 0],[0,2]]

test_invert_matrix()
print("All tests passed")