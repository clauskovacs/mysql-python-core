SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `books` (
isbn char(20) NOT NULL PRIMARY KEY,
title varchar(50),
author_id int(11),
publisher_id int(11),
year_pub char(4),
description text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `books` (`isbn`, `title`, `author_id`, `publisher_id`, `year_pub`, `description`) VALUES 
('0553213695', 'The Metamorphosis', 1, 'None', '1995', 'None'),
('0805210407', 'The Trial', 1, 'None', '1995', 'None'),
('0805210644', 'America', 1, 'None', '1995', 'None'),
('0805211063', 'The Castle', 1, 'None', '1998', 'None');

COMMIT;