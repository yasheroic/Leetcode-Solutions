class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Calculate x raised to the power n.

        Args:
            x (float): The base number.
            n (int): The exponent.

        Returns:
            float: The result of x raised to the power n.
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        return self.fastPow(x, n)

    def fastPow(self, x: float, n: int) -> float:
        """
        Helper function to calculate x raised to the power n using exponentiation by squaring.

        Args:
            x (float): The base number.
            n (int): The exponent.

        Returns:
            float: The result of x raised to the power n.
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n % 2 == 0:
            return self.fastPow(x * x, n // 2)
        else:
            return x * self.fastPow(x, n - 1)
