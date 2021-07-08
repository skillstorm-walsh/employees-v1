# employees-v1
Simple JSON server for training purposes. You can access more information about the API here:
https://my-json-server.typicode.com/pjw6193/employees-v1
HTTP operations like POST, PUT, and DELETE do not alter the underlying data.

GET https://my-json-server.typicode.com/pjw6193/employees-v1/employees
  - returns all employee (total of 3)
  - expected status code: 200

GET https://my-json-server.typicode.com/pjw6193/employees-v1/employees/{id}
  - returns an employee by ID
  - example: https://my-json-server.typicode.com/pjw6193/employees-v1/employees/1
  - expected status code: 200

POST https://my-json-server.typicode.com/pjw6193/employees-v1/employees
  - include employee JSON in the request body
  - simulates adding a new employee
  - expected status code: 201 

PUT https://my-json-server.typicode.com/pjw6193/employees-v1/employees/1
  - include employee JSON in the request body
  - simulates updating an employee
  - expected status code: 200

DELETE https://my-json-server.typicode.com/pjw6193/employees-v1/employees/1
  - simulates deleting an employee
  - expected status code: 200
