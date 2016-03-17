# README #

This project supports reading stache via the API.

### What is this repository for? ###

* Summary: This project supports reading stache entries via the stache API. 
There is an expectation that entires are in a specific format, based on what 
the entry is for. 

* Version: 1.0

### How do I get set up? ###

* Check out this repository

* Get a virtual environment (e.g., pyvenv) set up and pip install the
  requirements file once the virtualenv has been activated.

* How to run tests

    * Requirements not listed in requirements.txt
        * coverage >= 
        * nose >= 1.3.7
        * PyYAML >= 2.8.1


### Stache Format guidelines ###

* All Entires that will be accessed from this package need the option to "allow
 this item to be accessed by read-only API calls" enabled on the Stache entry

* Workday ISUs
    * Nickname is the username
    * Password is in secret
    * Each tenant will have its own entry - this may be changed in the future
    * It will be the responsibility of the calling program to append @tenant as 
    needed

* Oracle
    * Nickname is the oracle user
    * Secret holds passwords for all environments
        * Ex: DEV: password-dev
              QUAL: password-qual
              PROD: password-prod

* Unhandled Situations
    * multi environment credentials
    * multi-tenant credentials
    * credentials for anything outside workday ISUs and Oracle
    * Connection strings for Oracle
    * ?

### How to Call ###

* There are multiple ways to get data out of stache depending on your needs:

    * ISU.get_credentials is used for returning the username, password for a 
    Workday ISU.  There is no logic to deal with different tenants.
    
    * oracle.get_credentials is used for returning an oracle user and password 
    for a passed in environment (DEV, QUAL, or PROD)
    
    * all_fields.get_stache_entry can be used to return a list of all fields in 
    a stache entry, without any kind of parsing.  This is useful for new or 
    unique stache entries.

### Contribution guidelines ###

You are expected to write tests for any new functionality you add.

### Who do I talk to? ###

* [ASMP Integrations Tech Team](mailto:asmp-erp.integrations-tech@austin.utexas.edu)