use bramanud_db;
drop table if exists experiences;
drop table if exists tags;
drop table if exists reviews;
drop table if exists keywords;
drop table if exists companies;
create table reviews (
       r_id int primary key,
       text varchar(500),
       pos_sentiment boolean,
       job_title varchar(500)
);

-- insert into reviews values
--        (1, 'this racist company is very bad', false, 'senior engineer'),
--        (2, 'they are mean', false, 'product engineer');


create table keywords (
t_label varchar(50) primary key
);
-- insert into keywords values
--        ('sexism'),
--        ('terrible'),
--        ('sad');


create table tags (
       r_id int,
       t_label varchar(50),
       foreign key (r_id) references reviews on delete cascade,
       foreign key (t_label) references keywords on delete cascade, 
);
ENGINE = InnoDB;
-- insert into tags(r_id, t_label) values
--        (1, 'sexism'),
--        (1, 'terrible'),
--        (2, 'sad');


create table companies (
c_name varchar(50) primary key,
);
-- insert into keywords(c_name) values
--        ('Target'),
--        ('Google'),
--        ('Home Depot');


create table experiences (
       r_id int,
c_name varchar(50),
foreign key (r_id) references reviews on delete cascade,
foreign key (c_name) references companies on delete cascade
);
ENGINE = InnoDB;
-- insert into tags(r_id, c_name) values
--        (1, 'Target'),
--        (5, 'Target'),
--        (6, 'Google');



