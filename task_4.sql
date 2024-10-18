-- Use the alx_book_store database
USE alx_book_store;

-- Select the full description of the table Books
SELECT 
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    CHARACTER_MAXIMUM_LENGTH
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_NAME = 'Books' AND TABLE_SCHEMA = 'alx_book_store';
