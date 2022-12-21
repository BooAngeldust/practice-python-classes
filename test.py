from vector import Vector3, Vector2

def test_vector2_add(a : Vector2, b : Vector2, result : Vector2):
    assert(a+b == result)


a = Vector2(2,3)
b = Vector2(3,2)

test_vector2_add(a,b, (5,5))

a = Vector2(-1,3)
b = Vector2(3,-2)

test_vector2_add(a,b, (2,1))

a = Vector2(0,0)
b = Vector2(0,0)

test_vector2_add(a,b, (0,0))


