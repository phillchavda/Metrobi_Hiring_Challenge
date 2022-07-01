import unittest
import question5

class TestFunc(unittest.TestCase):

    def setUp(self):

        with open('question5_input.txt', 'r') as input_file:
            self.input_list = input_file.readlines()

        with open('question5_output.txt', 'r') as output_file:
            self.expected_outputs = output_file.readlines()


    def test_v1(self):

        with open('question5_results.txt', 'w') as results:
            results.write("Testing v1\n")

            for i in range(len(self.input_list)):

                self.input_list[i] = self.input_list[i].replace("\n", "")
                self.expected_outputs[i] = self.expected_outputs[i].replace("\n", "")

                output = str(question5.isPrimeNumber_v1(int(self.input_list[i])))
                if output != self.expected_outputs[i]:
                    results.write("input: " + self.input_list[i] + ", output: " + output + ", expected output: " + self.expected_outputs[i] + "\n")
            results.write("\n")

    def test_v2(self):

        with open('question5_results.txt', 'a') as results:
            results.write("Testing v2\n")
            
            for i in range(len(self.input_list)):

                self.input_list[i] = self.input_list[i].replace("\n", "")
                self.expected_outputs[i] = self.expected_outputs[i].replace("\n", "")

                output = str(question5.isPrimeNumber_v2(int(self.input_list[i])))
                if output != self.expected_outputs[i]:
                    results.write("input: " + self.input_list[i] + ", output: " + output + ", expected output: " + self.expected_outputs[i] + "\n")
            results.write("\n")


if __name__ == '__main__':
    unittest.main()