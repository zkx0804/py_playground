# problem set 1


class Problem1:
    p_name = "Campus bikes. LC1057/1066"
    p_description = {'algorithm': "Hungarian Maximum Matching Algorithm (KM, O(n^3))",
                     'link': "https://brilliant.org/wiki/hungarian-matching/"
                     }
    input_args = None

    def __init__(self):
        pass

    def solve(self, input_args):
        if not input_args and not self.input_args:
            print("No args found.")
            return None

        print("Input: \r%s" % self.input_args)

        print("Done!")


if __name__ == "__main__":
    # Run actual funcs
    print('Run!')
