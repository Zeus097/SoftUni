from project.integer_list import IntegerList


from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList([1, '20', 2.5, True])

    def test_integer_list_initialisation(self):
        self.integer_list = [1, 2, 3]
        self.assertEqual([1, 2, 3], self.integer_list)

    def test_integer_list_add_floating_number(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(1.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_integer_list_add_integer_number(self):
        self.integer_list = IntegerList([])
        self.integer_list.add(5)
        self.assertEqual([5], self.integer_list.get_data())

    def testing_get_data_method(self):
        self.assertEqual([], self.integer_list.get_data())

    def test_remove_index_case_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(100)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_index_in_range(self):
        self.integer_list.add(1)
        self.integer_list.remove_index(0)
        self.assertEqual([], self.integer_list.get_data())

    def test_get_index_case_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(50)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_index_with_index_in_range(self):
        self.integer_list.add(1)
        self.integer_list.get_index(1)
        self.assertEqual([1], self.integer_list.get_data())

    def test_insert_case_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(1, 10)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_case_with_float_element(self):
        self.integer_list.add(1)
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, 5.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_case_with_index_in_range(self):
        self.integer_list.add(1)
        self.integer_list.insert(0, 1)
        self.assertEqual([1, 1], self.integer_list.get_data())

    def test_get_biggest_case(self):
        self.integer_list.add(20)
        self.integer_list.add(50)
        self.integer_list.get_biggest()
        self.assertEqual(50, self.integer_list.get_biggest())

    def test_get_index_case(self):
        self.integer_list.add(1)
        self.integer_list.get_index(1)
        self.assertEqual([1], self.integer_list.get_data())


if __name__ == '__main__':
    main()
