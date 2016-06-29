# README #

This project supports reading stache via the API.

### What is this repository for? ###

* Summary: This project supports reading stache entries via the stache API. 
There is an expectation that entires are in a specific format, based on what 
the entry is for. 

* [Stache API Wiki Page](https://wikis.utexas.edu/display/ISO/Stache+API)

* Version: 1.0

### How do I get set up? ###

* Check out this repository

* Get a virtual environment (e.g., pyvenv) set up and pip install the
  requirements file once the virtualenv has been activated.

* How to run tests

    * tests expect a test_config.yaml.  See the test_config_example.yaml for 
      expected format.
    * install dev_requirements.txt
    * nosetests
    * this also displays your coverage stats - they should stay about 80%


### Stache Format guidelines ###

* All Entires that will be accessed from this package need the option to "allow
 this item to be accessed by read-only API calls" enabled on the Stache entry

* Parsed Environment
    * Nickname is the username
    * Secret holds passwords for all environments/tenants/etc

Ex (Oracle)

```
DEV: password-dev
QUAL: password-qual
PROD: password-prod
```

Ex  (ISU)

```
utaustin6: password123
utaustin9: passwordABC
```

* Unhandled Situations
    * Connection strings for Oracle
    * ?

### How to Call ###

* There are multiple ways to get data out of stache depending on your needs:

    * parsed_env.get_credential is used for returning the username and password 
    for a passed in environment.)
    
    * all_fields.get_stache_entry can be used to return a list of all fields in 
    a stache entry, without any kind of parsing.  This is useful for new or 
    unique stache entries.

### Contribution guidelines ###

You are expected to write tests for any new functionality you add.

### Who do I talk to? ###

* [ASMP Integrations Tech Team](mailto:asmp-erp.integrations-tech@austin.utexas.edu)