def sum_of_squares(a):
	answer = 0
	for x in a:
		answer += (x*x)
	return answer

def test_one():
    assert sum_of_squares([1,2,3]) == 14, "False"

def test_two():
	assert sum_of_squares([1,2,3,4]) == 30, "False"

test_one()
test_two()
