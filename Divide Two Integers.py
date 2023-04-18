class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge cases
        if divisor == 0:
            return 0

        if dividend == 0:
            return 0

        if divisor == 1:
            return dividend

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign of the quotient
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert dividend and divisor to positive integers
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize quotient and divisor_sum to 0
        quotient = 0
        divisor_sum = 0

        # Iterate through the bits of dividend from left to right
        for i in range(31, -1, -1):
            # Update divisor_sum by shifting it to the left by 1
            divisor_sum = divisor_sum << 1

            # Set the least significant bit of divisor_sum to the i-th bit of dividend
            divisor_sum |= (dividend >> i) & 1

            # If divisor_sum is greater than or equal to divisor, subtract divisor from divisor_sum
            if divisor_sum >= divisor:
                divisor_sum -= divisor
                quotient |= 1 << i

        # Return the quotient with the appropriate sign
        return sign * quotient
