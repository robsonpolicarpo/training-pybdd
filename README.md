# Integration Tests

###### Integrations tests (end2end) using BDD, Web, API and Mobile tests with Python and Selenium frameworks

#### Requirements

* Python 3.8
* pip
* pipenv (optional)
* npm (if you want to see html report)

#### Local Run

##### Install dependencies

```
 pipenv install
```

##### Set chromedriver in system path

```
 ./setup_chromedriver.sh
```

##### Run tests

```
pipenv run pytest \
-n=2 \
-k 'automating' \
--remote='false' \
--ipenv='localhost' \
--headless=false \
--tb=short \
--cucumberjson='./test-results/json/result.json' \
--cucumberjson-expanded
```

#### Report

```
npm install multiple-cucumber-html-reporter
```

- --cucumberjson-expanded 
- --alluredir='./test-results/allure' 
- --cucumberjson='./test-results/json/result.json'

#### References

* [test-goals](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/)
* [selene](https://github.com/OlenaOKushnir/selene)
* [bdd-and-testrail](https://moduscreate.com/blog/pytest-bdd-and-testrail-integration-test-artifacts/)
