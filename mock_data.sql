
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    account_type ENUM('root', 'admin', 'user') NOT NULL,
    full_name NVARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    apartment_code VARCHAR(50) PRIMARY KEY,
    email VARCHAR(255) DEFAULT NULL,
    dob DATE DEFAULT NULL,
    gender ENUM('male','female','undefined') DEFAULT NULL,
    id_card VARCHAR(20) DEFAULT NULL,
    hometown NVARCHAR(255) DEFAULT NULL
);

-- Create the fees table
CREATE TABLE IF NOT EXISTS fees (
    fee_name VARCHAR(50) PRIMARY KEY,
    deadline DATETIME,
    total INT DEFAULT 0,
    paid INT DEFAULT 0,
    remain INT DEFAULT 0,
    type ENUM('required', 'unrequired') NOT NULL
);

-- Create the userfee table
CREATE TABLE IF NOT EXISTS userfee (
    apartment_code VARCHAR(50) NOT NULL,
    fee_name VARCHAR(50) NOT NULL,
    total INT,
    paid INT,
    remain INT,
    FOREIGN KEY (apartment_code) REFERENCES users(apartment_code),
    FOREIGN KEY (fee_name) REFERENCES fees(fee_name)
);

-- Create the noti table
CREATE TABLE IF NOT EXISTS noti (
    apartment_code VARCHAR(50) NOT NULL,
    apartment_code2 VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (apartment_code) REFERENCES users(apartment_code),
    FOREIGN KEY (apartment_code2) REFERENCES users(apartment_code)
);

-- Trigger to update the `paid` column in `fees` after INSERT on `userfee`
DELIMITER $$

DROP TRIGGER IF EXISTS update_fees_paid$$
CREATE TRIGGER update_fees_paid
AFTER INSERT ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET paid = (
        SELECT COALESCE(SUM(paid), 0)
        FROM userfee
        WHERE fee_name = NEW.fee_name
    )
    WHERE fee_name = NEW.fee_name;
END$$

DROP TRIGGER IF EXISTS update_fees_paid2$$
CREATE TRIGGER update_fees_paid2
AFTER DELETE ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET paid = (
        SELECT COALESCE(SUM(paid), 0)
        FROM userfee
        WHERE fee_name = OLD.fee_name
    )
    WHERE fee_name = OLD.fee_name;
END$$

DROP TRIGGER IF EXISTS update_fees_paid3$$
CREATE TRIGGER update_fees_paid3
AFTER UPDATE ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET paid = (
        SELECT COALESCE(SUM(paid), 0)
        FROM userfee
        WHERE fee_name = NEW.fee_name
    )
    WHERE fee_name = NEW.fee_name;
END$$

DELIMITER ;

DELIMITER $$

DROP TRIGGER IF EXISTS update_fees_total$$
CREATE TRIGGER update_fees_total
AFTER INSERT ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET total = (
        SELECT COALESCE(SUM(total), 0)
        FROM userfee
        WHERE fee_name = NEW.fee_name
    )
    WHERE fee_name = NEW.fee_name;
END$$

DROP TRIGGER IF EXISTS update_fees_total2$$
CREATE TRIGGER update_fees_total2
AFTER DELETE ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET total = (
        SELECT COALESCE(SUM(total), 0)
        FROM userfee
        WHERE fee_name = OLD.fee_name
    )
    WHERE fee_name = OLD.fee_name;
END$$

DROP TRIGGER IF EXISTS update_fees_total3$$
CREATE TRIGGER update_fees_total3
AFTER UPDATE ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET total = (
        SELECT COALESCE(SUM(total), 0)
        FROM userfee
        WHERE fee_name = NEW.fee_name
    )
    WHERE fee_name = NEW.fee_name;
END$$

DELIMITER ;
DELIMITER $$

DROP TRIGGER IF EXISTS update_fees_remain$$
CREATE TRIGGER update_fees_remain
AFTER INSERT ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET remain = (
        SELECT COALESCE(SUM(remain), 0)
        FROM userfee
        WHERE fee_name = NEW.fee_name
    )
    WHERE fee_name = NEW.fee_name;
END$$

DROP TRIGGER IF EXISTS update_fees_remain2$$
CREATE TRIGGER update_fees_remain2
AFTER DELETE ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET remain = (
        SELECT COALESCE(SUM(remain), 0)
        FROM userfee
        WHERE fee_name = OLD.fee_name
    )
    WHERE fee_name = OLD.fee_name;
END$$

DROP TRIGGER IF EXISTS update_fees_remain3$$
CREATE TRIGGER update_fees_remain3
AFTER UPDATE ON userfee
FOR EACH ROW
BEGIN
    UPDATE fees
    SET remain = (
        SELECT COALESCE(SUM(remain), 0)
        FROM userfee
        WHERE fee_name = NEW.fee_name
    )
    WHERE fee_name = NEW.fee_name;
END$$

DELIMITER ;


INSERT INTO users (username, password, account_type, full_name, phone_number, apartment_code, email, dob, gender, id_card, hometown)
VALUES
    ('user1', 'password1', 'user', 'User 1', '0900000001', 'APT0001', 'user1@example.com', '1990-01-01', 'male', 'ID0001', 'Hometown 1'),
    ('user2', 'password2', 'user', 'User 2', '0900000002', 'APT0002', 'user2@example.com', '1990-01-02', 'female', 'ID0002', 'Hometown 2'),
    ('user3', 'password3', 'user', 'User 3', '0900000003', 'APT0003', 'user3@example.com', '1990-01-03', 'male', 'ID0003', 'Hometown 3'),
    ('user4', 'password4', 'user', 'User 4', '0900000004', 'APT0004', 'user4@example.com', '1990-01-04', 'female', 'ID0004', 'Hometown 4'),
    ('user5', 'password5', 'user', 'User 5', '0900000005', 'APT0005', 'user5@example.com', '1990-01-05', 'male', 'ID0005', 'Hometown 5'),
    ('user6', 'password6', 'user', 'User 6', '0900000006', 'APT0006', 'user6@example.com', '1990-01-06', 'female', 'ID0006', 'Hometown 6'),
    ('user7', 'password7', 'user', 'User 7', '0900000007', 'APT0007', 'user7@example.com', '1990-01-07', 'male', 'ID0007', 'Hometown 7'),
    ('user8', 'password8', 'user', 'User 8', '0900000008', 'APT0008', 'user8@example.com', '1990-01-08', 'female', 'ID0008', 'Hometown 8'),
    ('user9', 'password9', 'user', 'User 9', '0900000009', 'APT0009', 'user9@example.com', '1990-01-09', 'male', 'ID0009', 'Hometown 9'),
    ('user10', 'password10', 'user', 'User 10', '0900000010', 'APT0010', 'user10@example.com', '1990-01-10', 'female', 'ID0010', 'Hometown 10'),
    ('user11', 'password11', 'user', 'User 11', '0900000011', 'APT0011', 'user11@example.com', '1990-01-11', 'male', 'ID0011', 'Hometown 11'),
    ('user12', 'password12', 'user', 'User 12', '0900000012', 'APT0012', 'user12@example.com', '1990-01-12', 'female', 'ID0012', 'Hometown 12'),
    ('user13', 'password13', 'user', 'User 13', '0900000013', 'APT0013', 'user13@example.com', '1990-01-13', 'male', 'ID0013', 'Hometown 13'),
    ('user14', 'password14', 'user', 'User 14', '0900000014', 'APT0014', 'user14@example.com', '1990-01-14', 'female', 'ID0014', 'Hometown 14'),
    ('user15', 'password15', 'user', 'User 15', '0900000015', 'APT0015', 'user15@example.com', '1990-01-15', 'male', 'ID0015', 'Hometown 15'),
    ('user16', 'password16', 'user', 'User 16', '0900000016', 'APT0016', 'user16@example.com', '1990-01-16', 'female', 'ID0016', 'Hometown 16'),
    ('user17', 'password17', 'user', 'User 17', '0900000017', 'APT0017', 'user17@example.com', '1990-01-17', 'male', 'ID0017', 'Hometown 17'),
    ('user18', 'password18', 'user', 'User 18', '0900000018', 'APT0018', 'user18@example.com', '1990-01-18', 'female', 'ID0018', 'Hometown 18'),
    ('user19', 'password19', 'user', 'User 19', '0900000019', 'APT0019', 'user19@example.com', '1990-01-19', 'male', 'ID0019', 'Hometown 19'),
    ('user20', 'password20', 'user', 'User 20', '0900000020', 'APT0020', 'user20@example.com', '1990-01-20', 'female', 'ID0020', 'Hometown 20'),
    ('user21', 'password21', 'user', 'User 21', '0900000021', 'APT0021', 'user21@example.com', '1990-01-21', 'male', 'ID0021', 'Hometown 21'),
    ('user22', 'password22', 'user', 'User 22', '0900000022', 'APT0022', 'user22@example.com', '1990-01-22', 'female', 'ID0022', 'Hometown 22'),
    ('user23', 'password23', 'user', 'User 23', '0900000023', 'APT0023', 'user23@example.com', '1990-01-23', 'male', 'ID0023', 'Hometown 23'),
    ('user24', 'password24', 'user', 'User 24', '0900000024', 'APT0024', 'user24@example.com', '1990-01-24', 'female', 'ID0024', 'Hometown 24'),
    ('user25', 'password25', 'user', 'User 25', '0900000025', 'APT0025', 'user25@example.com', '1990-01-25', 'male', 'ID0025', 'Hometown 25'),
    ('user26', 'password26', 'user', 'User 26', '0900000026', 'APT0026', 'user26@example.com', '1990-01-26', 'female', 'ID0026', 'Hometown 26'),
    ('user27', 'password27', 'user', 'User 27', '0900000027', 'APT0027', 'user27@example.com', '1990-01-27', 'male', 'ID0027', 'Hometown 27'),
    ('user28', 'password28', 'user', 'User 28', '0900000028', 'APT0028', 'user28@example.com', '1990-01-28', 'female', 'ID0028', 'Hometown 28'),
    ('user29', 'password29', 'user', 'User 29', '0900000029', 'APT0029', 'user29@example.com', '1990-01-29', 'male', 'ID0029', 'Hometown 29'),
    ('user30', 'password30', 'user', 'User 30', '0900000030', 'APT0030', 'user30@example.com', '1990-01-30', 'female', 'ID0030', 'Hometown 30');

INSERT INTO fees (fee_name, deadline, type)
VALUES
    ('Electricity 12/2024', '2024-12-30', 'required'),
    ('Water 12/2024', '2024-12-30', 'required'),
    ('Maintenance 12/2024', '2024-12-30', 'required'),
    ('Parking 12/2024', '2024-12-30', 'required'),
    ('Electricity 01/2025', '2025-01-31', 'required'),
    ('Water 01/2025', '2025-01-31', 'required'),
    ('Maintenance 01/2025', '2025-01-31', 'required'),
    ('Parking 01/2025', '2025-01-31', 'required');
    
INSERT INTO fees (fee_name, deadline, type)
VALUES
    ('Save the Dogs', '2024-12-20', 'unrequired'),
    ('Save the Cats', '2024-12-15', 'unrequired'),
    ('Tet Holiday For Poor Students', '2024-12-25', 'unrequired'),
    ('Charity for SE11 Group', '2025-01-10', 'unrequired'),
    ('For a better future of SE11 Group', '2025-01-20', 'unrequired'),
    ('Save SE11', '2025-01-18', 'unrequired');

-- Insert required fees where total, paid, and remain are divisible by 1000
-- Insert required fees where total, paid, and remain are divisible by 1000
CREATE TEMPORARY TABLE temp_userfee AS
SELECT
    u.apartment_code,
    f.fee_name,
    CASE
        WHEN u.apartment_code LIKE 'APT0001%' THEN 300000
        WHEN u.apartment_code LIKE 'APT0002%' THEN 500000
        WHEN u.apartment_code LIKE 'APT0003%' THEN 700000
        ELSE 1000000
    END AS total,
    0 AS paid,
    CASE
        WHEN u.apartment_code LIKE 'APT0001%' THEN 300000
        WHEN u.apartment_code LIKE 'APT0002%' THEN 500000
        WHEN u.apartment_code LIKE 'APT0003%' THEN 700000
        ELSE 1000000
    END AS remain
FROM
    users u
JOIN
    fees f ON f.type = 'required';
INSERT INTO userfee (apartment_code, fee_name, total, paid, remain)
SELECT apartment_code, fee_name, total, paid, remain
FROM temp_userfee;

INSERT INTO userfee (apartment_code, fee_name, total, paid, remain)
VALUES
    ('APT0014', 'Save the Dogs', 0, 300000, NULL), -- APT0014 pays 300,000
    ('APT0017', 'Save the Cats', 0, 400000, NULL), -- APT0017 pays 400,000
    ('APT0023', 'Tet Holiday For Poor Students', 0, 500000, NULL); -- APT0023 pays 500,000

INSERT INTO users (apartment_code, username, password, account_type, full_name, phone_number, email)
VALUES
    ('ADMIN0024', 'admin1', 'admin1', 'admin', 'Admin User', '0922222222', 'admin@example.com');

