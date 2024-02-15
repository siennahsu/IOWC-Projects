CREATE TABLE annualcycles (
	station character varying NOT NULL,
	month character varying,
	mean numeric,
	standard_deviation numeric,
	‘2_5‘ numeric,
	‘17‘ numeric,
	‘50‘ numeric,
	‘83‘ numeric,
	‘97_5‘ numeric
);



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


CREATE TABLE countrycodes (
	code integer NOT NULL,
	country character varying NOT NULL
);




CREATE TABLE prcp (
	station character varying NOT NULL,
	identifier bigint NOT NULL PRIMARY KEY,
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
