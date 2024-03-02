-- sql script


CREATE DATABASE IF NOT EXISTS MainPortfolio;
       CREATE USER IF NOT EXISTS 'main_portfolio'@'localhost' IDENTIFIED BY 'Iamdonpablo25_';
              GRANT ALL PRIVILEGES ON MainPortfolio.* TO 'main_portfolio'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'main_portfolio'@'localhost';
FLUSH PRIVILEGES;
