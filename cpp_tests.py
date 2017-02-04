import random
import unittest

from coderunner import File, CppRunner

template = '#include <iostream>\n' \
           '#include <string>\n' \
           'using namespace std;' \
           'int main() {' \
           '%code%' \
           '}'


class CppHelloWorld(unittest.TestCase):
    def runTest(self):
        runner = CppRunner(folder_name='helloworld', files=[File('HelloWorld.cpp', code=template.replace('%code%', 'cout << "Hello, world!" << endl;'))])
        success, output = runner.go()
        self.assertEqual(output, 'Hello, world!')
        runner.cleanup()


class CppEcho(unittest.TestCase):
    def runTest(self):
        runner = CppRunner(folder_name='echo', files=[File('Echo.cpp',
                           code=template.replace('%code%', 'string echo;getline(cin,echo);cout << echo << endl;'))])

        data = (
            ('Hello, world!', 'Hello, world!'),
            ('Goodbye, world!', 'Goodbye, world!')
        )

        for inp, correct in data:
            success, output = runner.go(inp)
            self.assertTrue(success)
            self.assertEqual(output, correct)

        runner.cleanup()


class CppEchoRandom(unittest.TestCase):
    def runTest(self):
        runner = CppRunner(folder_name='echo', files=[File('Echo.cpp',
                           code=template.replace('%code%', 'string echo;getline(cin,echo);cout << echo << endl;'))])

        data = [(str(num), str(num)) for num in [random.randint(1, 100) for _ in range(3)]]

        for inp, correct in data:
            success, output = runner.go(inp)
            self.assertTrue(success)
            self.assertEqual(output, correct)

        runner.cleanup()


if __name__ == '__main__':
    unittest.main()
