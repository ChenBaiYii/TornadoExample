create databases website default character set utf8;

use website;

create table website_user_info(
	ui_user_id bigint unsigned auto_increment comment "this is user info id",
	ui_name varchar(64) not null comment "username",
	ui_passwd varchar(128) not null comment "pass word",
	ui_age int unsigned null comment "age",
	ui_mobile char(12) not null comment "phone number",
	ui_avatar varchar(128) null comment "user image",
	ui_ctime datetime default current_timestamp comment "crete date time",
	ui_updatetime datetime default current_timestamp on update current_timestamp;
	primary key(ui_user_id),
	unique (ui_mobile),
) engine=InnoDB default charset=utf8 comment "user infomation tables";

create table website_hourse_info(
	hi_id bigint unsigned auto_increment comment "hourse id",
	hi_user_id bigint unsigned auto_increment comment "user id",
	hi_name varchar(64) not null comment "houser name",
	hi_address varchar(256) not null comment "address",
	hi_price int unsigned not null comment "price",
	hi_ctime datetime default current_timestamp comment "crete date time",
	hi_updatetime datetime default current_timestamp on update current_timestamp;
	primary key(hi_hourse_id),
	constraint foreign key (hi_hourse_id)

)

create table user_info (
id int not null auto_increment,
name varchar(64) not null, 
age int not null, 
content varchar(128) not null comment "the content", primary key (id));





create table website_hourse_image(
	hi_image_id bigint unsigned auto_increment comment "image id",
	hi_hourse_id bigint unsigned auto_increment comment "hourse id",
	hi_url varchar(128) not null comment "image url",
	hi_ctime datetime default current_timestamp comment "create time",
	hi_utime datetime default current_timestamp update current_timestamp comment "update time",
	primary key ()


)