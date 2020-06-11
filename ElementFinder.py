import bs4 as bs
from collections import defaultdict


class ElementFinder:
    def __init__(self, original_file, element_id, target_file):
        with open(target_file, 'r') as f:
            contents = f.read()

            self.data = bs.BeautifulSoup(contents, 'lxml')

        with open(original_file, 'r') as f:
            contents = f.read()

            soup = bs.BeautifulSoup(contents, 'lxml')
            self.element = soup.find(id=element_id)

    def print_path(self):
        path = self.get_path()
        print(path[0], end='')
        for item in path[1:]:
            print(' >', item, end='')
        print()

    def get_path(self):
        curr_element = self.locate_element()
        path = []

        while curr_element.parent:
            # check if element has previous siblings of the same type
            length = len(list(curr_element.find_previous_siblings(curr_element.name))) + 1
            if length > 1:
                path.append(f'{curr_element.name}[{str(length)}]')
            else:
                path.append(curr_element.name)

            curr_element = curr_element.parent
        path.reverse()

        return path

    def locate_element(self):
        # dict to store elements with similar attributes
        similar_elements = {}
        similar_elements = defaultdict(lambda: 0, similar_elements)

        for el in self.data.find_all():
            # increase score for elements with same element name as target element
            if self.element.name == el.name:
                similar_elements[el] += 1

            # check if elements have same attrs
            common_attrs = set(el.attrs).intersection(self.element.attrs)
            initial_el_score = similar_elements[el]

            # check if attr values are the same
            for attr in common_attrs:
                if el.get(attr) == self.element.get(attr):
                    similar_elements[el] += 1

            # check if any attr value matched and check element name and inner text
            if initial_el_score < similar_elements[el]:
                if el.name == self.element.name:
                    similar_elements[el] += 1
                common_words = set(el.text.split(' ')).intersection(self.element.text.split(' '))
                similar_elements[el] += len(common_words)

        return sorted(similar_elements.items(), key=lambda x: x[1], reverse=True)[0][0]
