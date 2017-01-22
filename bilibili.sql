create database bilibili;
use bilibili;
create table info_bilibili_video( 
  vid int NOT NULL,
  view int,
  danmaku int,
  reply int,
  favorite int,
  coin int,
  share int,
  his_rank int,
  PRIMARY KEY (vid)  
);
  