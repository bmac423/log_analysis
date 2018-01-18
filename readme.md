# Log Analyzer

### Summary

This project sets up a Postgres database for a fictional news website. You'll need to initialize the database in order to utilize the script in this repository. The script returns valuable information about the usage of the website.

The report contains answers to the following questions:

  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

### Setting Up the Database

#### Installing the Virtual Machine
One way to have an image up and running very quickly is to utilize Udacity's pre-baked Vagrant image. Otherwise, you'll have to setup Postgresql some other way. Udacity provides a Linux machine that has Postgresql installed and configured. There are instructions available for the setup here (You must be a student for these links to work.):

<a href="https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0">Installing the Virtual Machine</a>


You can download the image here:

<a href="http://video.udacity-data.com.s3.amazonaws.com/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip">Vagrant Box</a>

#### Adding the Database
Once you have a working Postgresql system, you're ready to add the *News* database.

  1. From your Vagrant directory, download the data from the url provided:

    ```wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip```

  2. Unzip the file.

    ```unzip newsdata.zip```

  3. You should now see the sql script file (*newsdata.sql*)for setting up the database in the directory. Add the database to your Postgres instance with the following command:

    ```psql -d news -f newsdata.sql```

### Running the Report
Now that you have the database running in your Postgres instance, you're ready to run the report.

  1. Clone this repo to your working directory.  

  2. Move into the repo path.

  3. Execute the script with the following (ensure appropriate permissions for exec):  
      ```./log_report.py```

  4. You should see output similar to the following:  

```          
**********


1. What are the most popular three articles of all time?


Candidate is jerk, alleges rival -- 338647
Bears love berries, alleges bear -- 253801
Bad things gone, say good people -- 170098


**********


2. Who are the most popular article authors of all time?


Ursula La Multa -- 507594
Rudolf von Treppenwitz -- 423457
Anonymous Contributor -- 170098
Markoff Chaney -- 84557


**********


3. On which days did more than 1% of requests lead to errors?


JULY     17, 2016 -- 2.3
```
