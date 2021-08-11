class Repository:

    def change_element_objID_to_str(self, elem: dict) -> None:
        elem['_id'] = str(elem['_id'])

    
    def change_list_elements_objID_to_str(self, elements: list) -> None:
        for elem in elements:
            self.change_element_objID_to_str(elem)
