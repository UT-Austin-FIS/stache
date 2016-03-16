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

    * TBD

* Deployment instructions

    * TBD

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

### Contribution guidelines ###

You are expected to write tests for any new functionality you add.

### Who do I talk to? ###

* [ASMP Integrations Tech Team](mailto:asmp-erp.integrations-tech@austin.utexas.edu)