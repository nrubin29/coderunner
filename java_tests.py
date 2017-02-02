import random
import unittest

from coderunner import JavaRunner, File

template = 'import java.util.Scanner;' \
           'public class %classname% {' \
           'public static void main(String[] args) {' \
           '%code%' \
           '}' \
           '}'


class JavaHelloWorld(unittest.TestCase):
    def runTest(self):
        runner = JavaRunner(folder_name='helloworld', files=[File('HelloWorld.java', code=template.replace('%classname%', 'HelloWorld').replace('%code%', 'System.out.println("Hello, world!");'))])
        success, output = runner.go()
        self.assertEqual(output, 'Hello, world!')
        runner.cleanup()


class JavaEcho(unittest.TestCase):
    def runTest(self):
        runner = JavaRunner(folder_name='echo', files=[File('Echo.java',
                            code=template.replace('%classname%', 'Echo').replace('%code%', 'Scanner s = new Scanner(System.in); System.out.println(s.nextLine());'))])

        data = (
            ('Hello, world!', 'Hello, world!'),
            ('Goodbye, world!', 'Goodbye, world!')
        )

        for inp, correct in data:
            success, output = runner.go(inp)
            self.assertTrue(success)
            self.assertEqual(output, correct)

        runner.cleanup()


class JavaEchoRandom(unittest.TestCase):
    def runTest(self):
        runner = JavaRunner(folder_name='echo', files=[File('Echo.java',
                            code=template.replace('%classname%', 'Echo').replace('%code%', 'Scanner s = new Scanner(System.in); System.out.println(s.nextLine());'))])

        data = [(str(num), str(num)) for num in [random.randint(1, 100) for _ in range(3)]]

        for inp, correct in data:
            success, output = runner.go(inp)
            self.assertTrue(success)
            self.assertEqual(output, correct)

        runner.cleanup()


if __name__ == '__main__':
    unittest.main()
