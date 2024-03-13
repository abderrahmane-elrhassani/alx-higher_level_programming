-- Script to convert the hbtn_0c_0 database to UTF-8
-- (UTF-8 multibyte, with utf8mb4_unicode_ci collation) in your MySQL server
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
