import random
import unittest

from coderunner import PythonRunner, File


class PythonHelloWorld(unittest.TestCase):
    def runTest(self):
        runner = PythonRunner(folder_name='helloworld', files=[File('helloworld.py', code='print("Hello, world!")')])
        success, output = runner.go()
        self.assertEqual(output, 'Hello, world!')
        runner.cleanup()


class PythonEcho(unittest.TestCase):
    def runTest(self):
        runner = PythonRunner(folder_name='echo', files=[File('echo.py', code='print(raw_input())')])

        data = (
            ('Hello, world!', 'Hello, world!'),
            ('Goodbye, world!', 'Goodbye, world!')
        )

        for inp, correct in data:
            success, output = runner.go(inp)
            self.assertTrue(success)
            self.assertEqual(output, correct)

        runner.cleanup()


class PythonEchoRandom(unittest.TestCase):
    def runTest(self):
        runner = PythonRunner(folder_name='echo', files=[File('echo.py', code='print(raw_input())')])

        data = [(str(num), str(num)) for num in [random.randint(1, 100) for _ in range(3)]]

        for inp, correct in data:
            success, output = runner.go(inp)
            self.assertTrue(success)
            self.assertEqual(output, correct)

        runner.cleanup()


if __name__ == '__main__':
    unittest.main()
