## **changed made**

**January 27, 2022**
ERD changed made from ERD-v1 to ERD-v2:
Added table diseases.
Created a Health_region _has_diseases.
Changed all relationships from health_region to Health_region _has_diseases.

## **ERD description**

ERD-V1 was designed to handle only 1 disease, ERD-V2 has been designed to handle multiple diseases. 

The information for 3 tables (health_regions, province, and country_regions) will be loaded in manually on creation of the database. These will require maintenance if the data changes in future. 
The Heath_region_has_diseases will be the central area for all queries to show the data. 

## **questions**

Have we missed something within our database?
Is there a better way to design this database?
Should the diseases table include more than just name? (discovery data, description, etc.)
Is the data about vaccination rates associated with a disease?

## **to be done**
Finalize ERD design.
Remake Data model.
Create table creation scripts for postgressql.  
Create insert scripts for static data .
Create scripts for common views.
Work with Adam to figure out if/how the init file will run the database scripts.
