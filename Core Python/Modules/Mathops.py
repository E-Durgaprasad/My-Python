"""Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance."""


class MathOps:
    @staticmethod
    def even(num):
        return num % 2 == 0


MathOps.even(3)
obj = MathOps()
print(MathOps.even)
obj.even(5)

