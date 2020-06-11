from ElementFinder import ElementFinder


e1 = ElementFinder(
    'test_files/original.htm',
    'make-everything-ok-button',
    'test_files/first_test.htm'
)
e1.print_path()

e2 = ElementFinder(
    'test_files/original.htm',
    'make-everything-ok-button',
    'test_files/second_test.htm'
)
e2.print_path()

e3 = ElementFinder(
    'test_files/original.htm',
    'make-everything-ok-button',
    'test_files/third_test.htm'
)
e3.print_path()

e4 = ElementFinder(
    'test_files/original.htm',
    'make-everything-ok-button',
    'test_files/forth_test.htm'
)
e4.print_path()