CREATE TABLE annualcycles (
	station character varying NOT NULL,
	month character varying,
	mean numeric,
	standard_deviation numeric,
	2_5 numeric,
	17 numeric,
	50 numeric,
	83 numeric,
	97_5 numeric
);

COPY annualcycles(station, month, mean, standard_deviation, 2_5, 17, 50, 83, 97_5)
FROM '/Users/Sienna/Desktop/IOWC_site/wetransfer_climate-database-files_2024-01-30_1943/annual_cycles_data.csv'
DELIMITER ','
CSV HEADER;



CREATE TABLE anomalies (
	station character varying NOT NULL,
	year integer NOT NULL,
	january numeric,
	february numeric,
	march numeric,
	april numeric,
	may numeric,
	june numeric,
	july numeric,
	august numeric,
	september numeric,
	october numeric,
	november numeric,
	december numeric
);

COPY anomalies(station, year, january, february, march, april, may, june, july, august, september, october, november, december)
FROM '/Users/Sienna/Desktop/IOWC_site/wetransfer_climate-database-files_2024-01-30_1943/anomaly_data.csv'
DELIMITER ','
CSV HEADER;



CREATE TABLE anomalies_percentages (
	station character varying NOT NULL,
	year integer NOT NULL,
	january numeric,
	february numeric,
	march numeric,
	april numeric,
	may numeric,
	june numeric,
	july numeric,
	august numeric,
	september numeric,
	october numeric,
	november numeric,
	december numeric
);

COPY anomalies_percentages(station, year, january, february, march, april, may, june, july, august, september, october, november, december)
FROM '/Users/Sienna/Desktop/IOWC_site/wetransfer_climate-database-files_2024-01-30_1943/anomaly_data.csv'
DELIMITER ','
CSV HEADER;



CREATE TABLE countrycodes (
	code integer NOT NULL,
	country character varying NOT NULL
);

COPY countrycodes(code, country)
FROM '/Users/Sienna/Desktop/IOWC_site/wetransfer_climate-database-files_2024-01-30_1943/country_codes.csv'
DELIMITER ','
CSV HEADER;



CREATE TABLE prcp (
	station character varying NOT NULL PRIMARY KEY,
	identifier bigint NOT NULL,
	year integer NOT NULL,
	january numeric,
	february numeric,
	march numeric,
	april numeric,
	may numeric,
	june numeric,
	july numeric,
	august numeric,
	september numeric,
	october numeric,
	november numeric,
	december numeric
);

COPY prcp(station, identifier, year, january, february, march, april, may, june, july, august, september, october, november, december)
FROM '/Users/Sienna/Desktop/IOWC_site/wetransfer_climate-database-files_2024-01-30_1943/detailed_prcp_data.csv'
DELIMITER ','
CSV HEADER;



CREATE TABLE stationmetadata (
	station character varying NOT NULL,
	identifier bigint NOT NULL,
	name character varying,
	region character varying,
	country character varying NOT NULL,
	latitude numeric NOT NULL,
	longitude numeric NOT NULL,
	elevation numeric,
	PRIMARY KEY(station, identifier)
);

COPY stationmetadata(station, identifier, name, region, country, latitude, longitude, elevation)
FROM '/Users/Sienna/Desktop/IOWC_site/wetransfer_climate-database-files_2024-01-30_1943/detailed_station_metadata_updated_regions.csv'
DELIMITER ','
CSV HEADER;