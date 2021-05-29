# Advertyzement Assignment for Backend

This simple project done for Advertyzement hiring process assessment.

### Problem Statement

Create a API server :

1. Data can be found in the [repository](https://github.com/snarayanank2/indian_banks) for the database. 
2. Any Python web framework can be used to create the API service.
3. It should support GraphQL calls at ‘/gql’.
4. It should have a query for querying Bank Branches data with all the sub class data.
5. Bonus points for clean code.
6. Bonus points for Test cases.
7. Bonus points for deploying it on services like Heroku.

### Deployment

This application is hosted on [heroku](https://advertyzement-susanka068.herokuapp.com/gql)

Link : https://advertyzement-susanka068.herokuapp.com/gql

### Instructions to run on your local system:

1. Clone this repository.

```bash
git clone https://github.com/susanka068/advertyzement_backend.git
```

2. If you're using it for the first time create the SQL database and insert the required values into the table. run : 

```bash
python3 data_insertion.py
```

a file *database.sqlite3* wwil be created in the project directory. This conatins the data on which queries will be executed.

3. start the server with the following 

```bash
python3 app.py
```

4. open your browser and go to [http://localhost:5000/gql](http://localhost:5000/gql) to view the graphql interface.

![deployment screenshot](https://github.com/susanka068/advertyzement_backend/blob/master/Screenshot%20from%202021-05-28%2010-03-41.png)
