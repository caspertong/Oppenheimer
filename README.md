# Oppenheimer Selenium UI Testing

1. Open the "Repo" folder from any IDE
2. Select test.py
3. Amend the directory of
	a. Chrome Driver
	b. csv file(test.csv) for upload
4. Open a terminal from the IDE, then type: pytest test.py::<TEST CASE NAME> -s
	which <TEST CASE NAME> is the test case name
	Example: pytest test.py::test_upload_csv -s