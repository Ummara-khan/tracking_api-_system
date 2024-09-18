# tracking_api-_system

Run it with Postman or Curl 

like this 

http://127.0.0.1:8000/api/next-tracking-number/?origin_country_id=1&destination_country_id=2&weight=10&customer_id=123&customer_name=John%20Doe&customer_slug=john-doe (change the values accordingly)



![image](https://github.com/user-attachments/assets/4039bf1e-cc90-4196-ae1c-698cc4922fdd)


Example Postman Request Configuration
Method: GET
URL: http://127.0.0.1:8000/next-tracking-number/
provide headers like this :

{
  "tracking_number": "RANDOMSTRING123456",
  "created_at": "2023-09-18T14:32:00+0000",
  "origin_country_id": "1",
  "destination_country_id": "2",
  "weight": "10",
  "customer_id": "123",
  "customer_name": "John Doe",
  "customer_slug": "john-doe"
}

