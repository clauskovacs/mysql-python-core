SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

INSERT INTO `books` (`isbn`, `title`, `author_id`, `publisher_id`, `year_pub`, `description`) VALUES 
('0553213695', 'The Metamorphosis', 1, 'None', '1991', 'None'),
('0805210407', 'The Trial', 1, 'None', '1992', 'None'),
('0805210644', 'America', 1, 'None', '1993', 'None'),
('0805211063', 'The Castle', 1, 'None', '1994', 'None'),
(1, 'The Castle', 1, 0, '1998', 'None');

COMMIT;
