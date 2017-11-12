use bramanud_db;
SET FOREIGN_KEY_CHECKS = 0;
drop table if exists experiences;
drop table if exists tags;
drop table if exists reviews;
drop table if exists companies;
drop table if exists keywords;
SET FOREIGN_KEY_CHECkS = 1;

create table companies (
        c_name varchar(50) primary key
)
ENGINE = InnoDB;

create table reviews (
       r_id varchar(50) primary key,
       c_name varchar(50) not null,
       post varchar(50),
       pos_sentiment boolean,
       job_title varchar(500),
       foreign key (c_name) references companies(c_name) on delete restrict
)

ENGINE = InnoDB;


create table keywords (
	t_label varchar(50) primary key
)

ENGINE = InnoDB;

create table tags (
       r_id varchar(50) not null,
       t_label varchar(50) not null,
       foreign key (r_id) references reviews(r_id) on delete restrict,
       foreign key (t_label) references keywords(t_label) on delete restrict
)

ENGINE = InnoDB;

create table experiences (
        r_id varchar(50) not null,
	c_name varchar(50) not null,
	foreign key (r_id) references reviews(r_id) on delete restrict,
	foreign key (c_name) references companies(c_name) on delete restrict
)

ENGINE = InnoDB;

-- insert into experiences values
--        (1, 'Target'),
--        (5, 'Target'),
--        (6, 'Google');



