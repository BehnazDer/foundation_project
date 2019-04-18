DROP TABLE IF EXISTS users;

    create table users (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
    username text not null,
    password text not null,
    repeat password text not null,
);

DROP TABLE IF EXISTS feedback;
    create table feedback (
    id integer primary key autoincrement,
    firstname text not null,
    lastname text not null,
    comment text nut null,
    );