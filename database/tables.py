TABLES = [ x.replace("\n", " ") for x in [
        """
        CREATE TABLE USER(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            contact VARCHAR(12),
            email VARCHAR(50),
            address VARCHAR(180)
        );
        """,
        """
        CREATE TABLE TEAM(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            manager INT,
            description VARCHAR(180),
            CONSTRAINT `TEAM_manager_fk` FOREIGN KEY (`manager`) REFERENCES `USER` (`id`)	ON DELETE SET NULL
        );
        """,
        """
        CREATE TABLE MEMBERSHIP(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            team INT,
            user INT,
            remarks VARCHAR(30),
            CONSTRAINT `Membership_team_fk` FOREIGN KEY (`team`) REFERENCES `TEAM` (`id`)	ON DELETE CASCADE,
            CONSTRAINT `Membership_user_fk` FOREIGN KEY (`user`) REFERENCES `USER` (`id`)	ON DELETE CASCADE
        );
        """,
    ]
]
