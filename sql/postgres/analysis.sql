CREATE TABLE teachers(
    id bigserial,
    first_name varchar(50),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Janet','Smith','F. D. Roosevelt HS', '2011-10-30', 36200),
        ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
        ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
        ('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
        ('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
        ('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
        ('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);


SELECT DISTINCT school FROM teachers;
SELECT first_name, last_name, salary FROM teachers ORDER BY salary DESC;
SELECT last_name, school, hire_date FROM teachers ORDER BY school ASC, hire_date DESC;
SELECT last_name, school, hire_date FROM teachers WHERE school = 'Myers Middle School';

= Equal to WHERE school = 'Baker Middle'
<> or != Not equal to* WHERE school <> 'Baker Middle'
> Greater than WHERE salary > 20000
< Less than WHERE salary < 60500
>= Greater than or equal to WHERE salary >= 20000
<= Less than or equal to WHERE salary <= 60500
BETWEEN Within a range WHERE salary BETWEEN 20000 AND 40000
IN Match one of a set of values WHERE last_name IN ('Bush','Roush')
LIKE Match a pattern (case sensitive) WHERE first_name LIKE 'Sam%'
ILIKE Match a pattern (case insensitive) WHERE first_name ILIKE 'sam%'
NOT Negates a condition WHERE first_name NOT ILIKE 'sam%'
Percent sign (%) A wildcard matching one or more characters
Underscore (_) A wildcard matching just one character

SELECT school FROM teachers WHERE school != 'F.D. Roosevelt HS';
SELECT first_name, last_name, hire_date FROM teachers WHERE hire_date < '2000-01-01';
SELECT first_name, last_name, salary FROM teachers WHERE salary >= 43500;
SELECT first_name, last_name, school, salary FROM teachers WHERE salary BETWEEN 40000 AND 65000;
SELECT first_name FROM teachers WHERE first_name LIKE 'sam%';
SELECT first_name FROM teachers WHERE first_name ILIKE 'sam%';
SELECT * FROM teachers WHERE school = 'F.D. Roosevelt HS' AND (salary < 38000 OR salary > 40000);
SELECT first_name, last_name, school, hire_date, salary FROM teachers WHERE school LIKE '%Roos%' ORDER BY hire_date DESC;


char(n)
varchar(n)
text
smallint 2 bytes −32768 to +32767
integer 4 bytes −2147483648 to +2147483647
bigint 8 bytes −9223372036854775808 to +9223372036854775807
smallserial 2 bytes 1 to 32767
serial 4 bytes 1 to 2147483647
bigserial 8 bytes 1 to 9223372036854775807
numeric, decimal variable Fixedpoint Up to 131072 digits before the decimal point; up to 16383 digits after the decimal point
real 4 bytes Floating-point 6 decimal digits precision
double precision 8 bytes Floating-point 15 decimal digits precision
timestamp 8 bytes Date and time 4713 BC to 294276 AD
timestamp with time zone
date 4 bytes Date (no time) 4713 BC to 5874897 AD
time 8 bytes Time (no date) 00:00:00 to 24:00:00
interval 16 bytes Time interval +/− 178,000,000 years
Boolean
Geometric
Network address
UUID
XML and JSON

CREATE TABLE char_data_types (
    varchar_column varchar(10),
    char_column char(10),
    text_column text
);
INSERT INTO char_data_types
VALUES ('abc', 'abc', 'abc'),
        ('defghi', 'defghi', 'defghi');
COPY char_data_types TO 'C:\YourDirectory\typetest.txt' WITH (FORMAT CSV, HEADER, DELIMITER '|');

CREATE TABLE number_data_types ( numeric_column numeric(20,5), real_column real, double_column double precision);
INSERT INTO number_data_types VALUES
(.7, .7, .7),
(2.13579, 2.13579, 2.13579),
(2.1357987654, 2.1357987654, 2.1357987654);
SELECT * FROM number_data_types;

CREATE TABLE date_time_types (timestamp_column timestamp with time zone,interval_column interval);
INSERT INTO date_time_types VALUES ('2018-12-31 01:00 EST','2 days'),
('2018-12-31 01:00 -8','1 month'),
('2018-12-31 01:00 Australia/Melbourne','1 century'),
(now(),'1 week');
SELECT * FROM date_time_types;

SELECT timestamp_column interval_column, timestamp_column - interval_column AS new_date FROM date_time_types;


SELECT timestamp_column, CAST(timestamp_column AS varchar(10)) FROM date_time_types;
SELECT timestamp_column::varchar(10) FROM date_time_types;
SELECT numeric_column, CAST(numeric_column AS integer), CAST(numeric_column AS varchar(6)) FROM number_data_types;
SELECT CAST(char_column AS integer) FROM char_data_types;

--- 10 --
SELECT median_hh_income, pct_bachelors_hi