# Importance of API programming 
API programming is integral to modern software development, serving as the linchpin for seamless communication between diverse applications and enabling modularity, scalability, and cross-platform compatibility. Its significance lies in facilitating third-party integrations, saving development time through reuse, fostering innovation and collaboration, and contributing to the growth of interconnected software ecosystems. APIs are vital for mobile app development, data access, and integration, providing a standardized approach to securely access and transmit information. Overall, API programming plays a pivotal role in creating efficient, scalable, and interconnected software systems that power the digital landscape.

# API-project

I created a fully functioning API project for the Little Lemon restaurant so that the client application developers can use the APIs to develop web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders. 

I have used the following tools, sofware and framework

* Git
* Python
* Django
* PostgreSQL
* Postman(API testing and debugging tool)

In this project, I have proven my ability to:

* Create RESTful APIs and use standard HTTP methods (GET, POST, PUT, DELETE)
* Create endpoints
* Created API authentications using OAuth tokens
* Testing and debugging. Used Postman tool to test endpoints.


<br />

### User groups

Two user groups are created and random users are assigned from the Django admin panel. 

Manager

Delivery crew

Users not assigned to a group will be considered customers.

<br />

### Error check and proper status codes
Error messages with appropriate HTTP status codes for specific errors is being displayed. These include when someone requests a non-existing item, makes unauthorized API requests, or sends invalid data in a POST, PUT or PATCH request. 

<br />

<pre>
  Tokens created successfully
</pre>

![api3](https://github.com/batuhan6/API-project/assets/32600613/013d1e2f-a424-4e6a-92a5-3f46dd867b5d)



<pre>
  With manager role I have right to access menu-items list.
</pre>

![api1](https://github.com/batuhan6/API-project/assets/32600613/42455ebb-122d-4570-b9c1-4a49c3dc1b3b)

<!--
<img src="https://github.com/batuhan6/API-project/assets/32600613/42455ebb-122d-4570-b9c1-4a49c3dc1b3b" width=800 >
-->
<pre>
  With delivery crew role I am not authorized to access menu-items list.
</pre>

![api2](https://github.com/batuhan6/API-project/assets/32600613/c0b717e4-e77c-416c-b782-d0581d7d20b1)

<pre>
  a
</pre>
![api4](https://github.com/batuhan6/API-project/assets/32600613/8e8a226f-b744-4055-8109-2e4adc4aed75)

<pre>
 a
</pre>
 ![api5](https://github.com/batuhan6/API-project/assets/32600613/64f207cb-26b3-4656-a140-0d200ae203db)

<pre>
  a
</pre>
  ![api6](https://github.com/batuhan6/API-project/assets/32600613/459974dc-479a-4b14-a2c9-d380547725fb)





