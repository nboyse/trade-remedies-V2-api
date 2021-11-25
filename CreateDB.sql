CREATE TABLE apiV2 (
    id character varying(36) NOT NULL PRIMARY KEY,
    timestamp date,
    category character varying(200),
    value integer
);

INSERT INTO apiV2
VALUES ('1', '2021-03-01', 'flake8', '200');
