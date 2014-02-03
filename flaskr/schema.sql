drop table if exists entries;
create table entries(
  id integer primary key autoincrement,
  Event text not null,
  SDate date not null,
  STime time not null,
  FDate date not null,
  FTime time not null,
  Location text not null,
  Note text
);
