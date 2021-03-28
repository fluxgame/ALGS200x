def assert_equal(expected, actual, test_name):
    if actual == expected:
        print(test_name + " passed")
    else:
        print("FAILED: " + test_name + ", expected: " + str(expected) + ", actual: " + str(actual))
