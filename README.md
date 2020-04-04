# Customer_Management_Sys
CMS using lists, then OOPS, and then with mySQL.

TABLE STRUCTURE IN CMS:

CREATE TABLE cmscustomer(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
address VARCHAR(250),
mobile VARCHAR(15) UNIQUE NOT NULL);
