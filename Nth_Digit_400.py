class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1           # Start with 1-digit numbers
        l = 1               # The smallest number with 'digit' digits
        range_ = 9          # There are 9 numbers with 1-digit (1-9)

        # Find the correct range of numbers (1-digit, 2-digit, 3-digit, etc.)
        while n - (range_ * digit) > 0:
            n -= (range_ * digit)   # Remove digits from the current range
            digit += 1              # Move to the next digit length
            l += range_             # Move the starting number to the next range
            range_ *= 10            # Increase the range (9, 90, 900, etc.)

        # Now, determine which number and which digit in that number
        if n % digit == 0:
            num = l - 1 + n // digit        # Find the exact number
            return int(str(num)[digit - 1]) # Find the last digit of the number
        else:
            num = l + n // digit            # Find the exact number
            return int(str(num)[n % digit - 1]) # Find the specific digit
