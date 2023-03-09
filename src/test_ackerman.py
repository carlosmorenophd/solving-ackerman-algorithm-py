import ackerman

def test_convert_to_new():
    assert ackerman.convert_to_new("A(0, 1)") == "2", "should be 2"
    assert ackerman.convert_to_new("A(1, 0)") == "A(0,1)", "should be A(0,0)"
    assert ackerman.convert_to_new("A(2, 1)") == "A(1,A(2,0))", "should be A(1,A(2,0))"
    assert ackerman.convert_to_new("A(2, 2)") == "A(1,A(2,1))", "should be A(1,A(2,1))"
    assert ackerman.convert_to_new("A(2, 0)") == "A(1,1)", "should be A(1,1)"
def test_search_expression():
    equation = "A(1, A(2, 1))"
    index = ackerman.search_expression(equation)
    assert equation[index[0]] == "A", "Should be A"
    assert equation[index[1]] == ")", "Should be )"
    assert equation[index[0]:index[1]] == "A(2, 1)", "Should be A(2, 1)"
def test_ackerman30():
    testAckerman = "A(3,0)"    
    ackerman.get_ackerman(
        equation=testAckerman, 
        max_iteration=10, 
        path = 'run_test', 
        explain = False
    )
    

if __name__ == "__main__":
    test_convert_to_new()
    test_search_expression()
    test_ackerman30()
    print("Everything passed")    
