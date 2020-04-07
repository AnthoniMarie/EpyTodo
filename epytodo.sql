/* SQL file for Epytodo (Epitech) :) */
CREATE DATABASE IF NOT EXISTS epytodo;

USE epytodo;
CREATE TABLE user (
    user_id INT AUTO_INCREMENT primary key NOT NULL,
    username VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL
);
CREATE TABLE task (
    task_id INT AUTO_INCREMENT primary key NOT NULL,
    title VARCHAR(128) NOT NULL,
    begin DATETIME DEFAULT CURRENT_TIMESTAMP,
    end DATETIME,
    status ENUM("not started", "in progress", "done") DEFAULT "not started"
);
CREATE TABLE user_has_task (
    fk_user_id VARCHAR(50) NOT NULL,
    fk_task_id VARCHAR(50) NOT NULL
);
