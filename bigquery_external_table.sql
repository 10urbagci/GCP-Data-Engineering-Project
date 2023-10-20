-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `project.bike_data.external_table`
OPTIONS (
  format = 'CSV',
  uris = ['gs://transformed-data-for-de-project/transformed_bike_data.csv']
);

SELECT * FROM `project.bike_data.external_table` LIMIT 10;

--partition table
CREATE OR REPLACE TABLE `project.bike_data.partition_external_table`
PARTITION BY
  DATE(timestamp) AS
SELECT * FROM `project.bike_data.external_table`;