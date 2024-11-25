# Employee Search Service

## The service

The project is about an API that provides the following basic functionalities to retrieve and serve employee data from a data source. Typically, this would be some SQL database. However, for the sake of simplicity, in this task, you will use the two CSV files with fake data provided in the `./employees` folder.


#### 1. Getting employee (name, company, ... ) 

The first task is to seamlessly serving both data-sources with a single API.

- **Calling `GET /api/employees?name=:name` should return a JSON object containing the list of all the employees who matches the `:name`**.
- `:name` is an url-encoded string.
  - If `:name` is a single word, an entry is considered as a match if either of the `first_name` or `last_name` matches the `:name`.
  - When the `:name` is multiple words, an entry would be considered as a match if the last word matches the `last_name` and the rest matches the `first_name`.
- Returned objected has the following keys: `{ name, company, address, phone, email }`
  - The following rules apply:
      - `name` is full name, i.e, `first_name<space>last_name` .
      - `address` is constructed differently for UK and US.
        - For UK: `address, city, upper_case(county), postal, UK`.
        - For US: `address, city, state, zip, USA`.
      - The country's phone code prepended to the `phone`.
  
#### 2. Company wages
- **Calling `GET /api/wage_stats?company_name=:name&country=:country` should return an image object that shows the wage distribution of the given company**.
  - `country` is an optional query parameter with the following accepted values: `UK`, `US`.
    - If country is given, use only the data from the given country, otherwise all data should be considered.
  - The wage distribution is drawn everytime when this endpoint is called and returned as a response with `media_type` `"image/png"`.
  - **Hint**: You can use a library e.g., `matplotlib`, `seaborn` to draw the wage distribution.

