class FibonacciThousandDigit():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms.
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.
    """

    def __init__(self, max_length=1000):
        self.max_length = max_length
        self.index = 2       # argument for fib(n) function
        self.num_length = 1  # how many digits does self.index contain
        # arguments for fib(n) and calculated results
        self.calculated = {0: 0, 1: 1}

    def calculate_fib(self):
        while self.num_length < self.max_length:
            self.index += 1
            # calculates fib(n)
            self.number = self.calculations(self.index)
            # updates length of current fib(n) output
            self.num_length = len(str(self.number))
        return(f'Index: {self.index}, number: {self.calculations(self.index)}')

    def calculations(self, value):
        """
        each fib(n) output is calculated once and is put in
        fib results dictionary - "self.calculated"
        If there is need to use fib(n) again,
        it is simply retrieved from that dict
        """
        if value - 1 in self.calculated.keys():
            number_one = self.calculated[value - 1]
        else:
            number_one = self.calculations(value - 1)
            self.calculated[value - 1] = number_one
        if value - 2 in self.calculated.keys():
            number_two = self.calculated[value - 2]
        else:
            number_two = self.calculations(value - 2)
            self.calculated[value - 2] = number_two

        recursive_sum = number_one + number_two
        return(recursive_sum)


if __name__ == '__main__':
    task = FibonacciThousandDigit(1000)
    print(task.calculate_fib())
