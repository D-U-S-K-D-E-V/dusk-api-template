from app.classes.example import Example

class Test_Example():
    def test_DoesSummationWork(self):
        example: Example = Example()
        assert example.summation(1,2) == 3