import sys
from ElementFinder import ElementFinder

finder = ElementFinder(sys.argv[1], sys.argv[2], sys.argv[3])
finder.print_path()