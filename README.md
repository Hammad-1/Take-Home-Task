# Forsit Take-Home-Task (Backend)
## Running the project with docker-compose

You can run the service with docker compose. First, make sure you have Docker and docker compose installed on your system.

1. Clone the repository and navigate to the project directory.
2. Build the Docker image and run the pproject with : `docker compose up --build`
3. This will start the project in a Docker container and expose it on localhost:8000.
4. To access endpoints open localhost:8000/docs. This url  contains swagger documentation for the endpoints
5. To stop the container, you can press Ctrl-C in the terminal window where you ran docker compose up.
6. To load demo data into the database, first make the "load_data.sh" script executable by running the "chmod +x load_data.sh" command. Next, access the MySQL Docker container using the "docker exec -it <CONTAINER_ID> bash" command, and execute the "./load_data.sh" script inside the container.
7. If point 6 won't work then use this command to load data in db:
"sudo docker exec -i 'CONTAINER_ID' mysql -u 'USER_NAME' -pmysql 'DB_NAME' < ./demo_data.sql". You can see 'USER_NAME' and 'DB_NAME' from docker.ini

Note: If you encounter a "Permission denied" error when running a Docker command, you can resolve it by running the Docker command as the root user with sudo.


## Running the server locally

To run service locally. first, make sure you have python==3.7 and pipenv==2023.7.23 installed on your system.

1. Clone the repository and navigate to the project directory.
2. Run pipenv install to install all required packages.
3. Run pipenv shell to activate virtual environment.
4. Update "SQLALCHEMY_DATABASE_URL" in db.py change host to localhost from mysql and similarly update "sqlalchemy.url" in alembic.ini change host to localhost.
5. Run a local MySQL server and create the database with credentials stored in local.ini
6. Run "alembic upgrade head" to apply migrations
7. Run "uvicorn main:app --reload" to start server locally
8. To load demo_data run "chmod +x load_data.sh" to make "./load_data.sh" executable then run the load_data.sh script with "./load_data.sh"


# Breif Explanation of Endpoints

## Products
### 1. Read All products "/products/" GET
### 2. Read product by id "/products/{product_id}/" GET
### 3. Create products "/products/" POST
### 4. Update products "/products/{product_id}/" PATCH
### 5. Delete products "/products/{product_id}/" DELETE

## Sales
### 1. Read All Sales "/Sales/" GET
### 2. Filter Sales "/Sales/filter_sales" GET:
- User can query sales with "sales_id", "product_id", "category_id", "date", "date_range".
- For query by product_id  this  endpoint will show all the sales for that paroduct_id.
- For query by category_id this endpoint will show sales all the sales of all the products of - that category. 
- For query by date you need to provide date in query params in "year-month-day" format and this endpoint will show sales details of that day.
- For query by date range you need to provide start-date and end-date in "year-month-day" format and this endpoint will show sales details between start date and date.
### 3. Analyze Revenue "/Sales/revenue" GET
- Endpoints to analyze revenue on a daily, weekly, monthly, and annual basis.
- To query "daily" revenue enter "daily" in period param and date in "year-month-day" format. This endpoint will show the sum of that day.
- To query "weekly" revenue enter "weekly" in period param and date in "year-month-day" format.This endpoint will show revenue sum for the week, starting from the provided data day.
- To query "monthly" revenue enter "monthly" in period param and provide value for month and year param in integer. This endpint will show revenue sum for the provided month of provided year.
- To query "annual" revenue enter "annual" in period param and provide value for year in integer. This endpint will show revenue sum of provided year.

## Inventory
### 1. Read Inventory Status Of All Products "/inventory/inventory-status" GET
- Endpoint to view current inventory status for all products, including low stock alerts.
- If user provide value for "low_stock_threshold" it will calculate give status alert acording to value provide. Else it will give "Low Stock" if quantity is less than 10 and "In Stock" if quantity is greater than or equal to 10
### 2. Update Inventory "/inventory/ PATCH"
- Endpoint to update quantity of a product based on product id and quantity provided. 
### 3. Track Inventory Update "/inventory/track-inventory-update" GET
Endpoint to view logs of inventory update record based on product id. When inventory is updated inventory logs is stored in InventoryLogs table which can be viewed by this endpoint.

# Note
I intended to create integration tests for every endpoint and unit tests for every function with complex search queries. However, due to time constraints, I decided to prioritize working on the service's core functionalities. Writing tests for every endpoint or function I create is typically a part of my coding practice.
