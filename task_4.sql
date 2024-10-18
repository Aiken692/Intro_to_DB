-- Use the alx_book_store database
USE alx_book_store;

-- Query to get full description of the books table
SELECT 
    COLUMN_NAME AS 'Field',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM 
    information_schema.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'books';
