from War import War

import sys

def test_it(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def parity_test_suite():
    """
    The parity_test_suite() is designed to test the following:
      is_binary()
      is_div_by_sevens()
      split_into_sevens()
      extract_text(text)
    :return: None
    """
    test = War()
    # Testing the is_binary()
    print("Testing is_binary()")
    test_it(test.add_dealingPile() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    test.text = "0110310"
    test_it(test.is_binary() == False)

parity_test_suite()
