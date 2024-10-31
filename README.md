# Employee Search Service

## Introduction

Hello,

In this coding exercise you will be addressing an issue/task that is central to our day-to-day work: writing and maintaining micro-services. This exercise aims to test your ability to write services in Python that efficiently solve problems we have in our business.

**Please read this document carefully before starting, as it outlines your task, the constraints and by what criteria you will be evaluated.**

Use git to document your work. When finished, please raise a pull/merge request to the `master` branch with appropriate title and branch name. While raising the pull request, please bear in mind that your branch would be **squashed** into `master`.

We will look at the git history of your pull request to determine the way you approached this and the time you roughly spent on the task. **Please do not squash commits or bundle many unrelated changes into one large commit.**


## The service

You are tasked to implement an API that provides the following basic functionalities to retrieve and serve employee data from a data source. Typically, this would be some SQL database. However, for the sake of simplicity, in this task, you will use the two CSV files with fake data provided in the `./employees` folder.


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

If anything here is unclear, make reasonable assumptions and choose your implementation accordingly, document it in the README.

## Constraints

- You are free to choose your libraries/framework(s). You can expect us to have the typical tools such as git, docker, python, brew, apt, docker, pre-installed.
- While we do not expect a production-ready system from this task, it should not take more than something like `python <script>`, `docker run`, `./start.sh` to run your solution.
- Do not introduce any external dependencies (databases, caches, search engines, ...) to solve this task.
- Your push right will be revoked after the agreed upon time and the latest commit of your implementation will be the basis for your evaluation.
- Keep it simple: You are not expected to spend days on this - just demonstrate that you know how to write great software.

## Evaluation criteria

In general, you can think of the evaluation being a thorough peer review of your code. 
You will be evaluated by a number of criteria, among others:

- How well did you apply engineering best practices (general and language specific ones)?
- Is the service working as intended?
- How readable is your code?
- Does the service solve the problem
    - correctly?
    - efficiently?
- How easy would it be to adapt your code to support more countries?
- Is your code consistent in itself (styling, language constructs, ...)?
- Appropriate use of 3rd party code/modules
- We do **not** expect you to have a high test coverage, **BUT** it is important that you demonstrate that you know how to write testable code and provide a few tests that showcase this.
- Proper use of git
- Making good assumptions and documenting them


### Good luck!!
