USE semi2practica1;

CREATE TABLE COUNTRY(
    id int primary key identity,
    name varchar(100) not null
);

CREATE TABLE CONTINENT(
    id varchar(10) primary key,
    name varchar(100) not null
);

CREATE TABLE STATUS(
    id int primary key identity,
    name varchar(100) not null
);

CREATE TABLE PILOT(
    id int primary key identity,
    name varchar(100) not null
);

CREATE TABLE PASSENGER(
    id varchar(50) primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    gender varchar(8),
    age smallint,
    country_id int,
    foreign key (country_id) references COUNTRY(id)
);

CREATE TABLE AIRPORT(
    id int primary key identity,
    name varchar(100) not null,
    country_id int,
    continent_id varchar(10),
    foreign key (country_id) references COUNTRY(id),
    foreign key (continent_id) references CONTINENT(id)
);

CREATE TABLE FLIGHT(
    id int primary key identity,
    departure_date date not null,
    month_date smallint not null,
    year_date int not null,
    arrival_airport varchar(50) not null,
	passenger_id varchar(50),
    airport_id int,
    pilot_id int,
    status_id int,
	foreign key (passenger_id) references PASSENGER(id),
    foreign key (airport_id) references AIRPORT(id),
    foreign key (pilot_id) references PILOT(id),
    foreign key (status_id) references STATUS(id),
);
