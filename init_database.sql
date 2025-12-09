-- Table for course resources (lecture notes, materials)
CREATE TABLE IF NOT EXISTS course_resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) NOT NULL,
    course_name VARCHAR(255) NOT NULL,
    week_number INT NOT NULL,
    resource_title VARCHAR(255),
    resource_url TEXT NOT NULL,
    resource_type VARCHAR(50) DEFAULT 'lecture_notes',
    resource_order INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_course_week (course_code, week_number),
    INDEX idx_course_name (course_name)
);

-- Insert course resources data
-- Distributed and Cloud System Programming
INSERT INTO course_resources (course_code, course_name, week_number, resource_title, resource_url, resource_order) VALUES
('DCSP', 'Distributed and Cloud System Programming', 1, 'Week 1 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294026', 1),
('DCSP', 'Distributed and Cloud System Programming', 1, 'Week 1 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294028', 2),
('DCSP', 'Distributed and Cloud System Programming', 2, 'Week 2 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294032', 1),
('DCSP', 'Distributed and Cloud System Programming', 2, 'Week 2 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294033', 2),
('DCSP', 'Distributed and Cloud System Programming', 3, 'Week 3 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294037', 1),
('DCSP', 'Distributed and Cloud System Programming', 3, 'Week 3 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294038', 2),
('DCSP', 'Distributed and Cloud System Programming', 3, 'Week 3 - Resource 3', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294039', 3),
('DCSP', 'Distributed and Cloud System Programming', 3, 'Week 3 - Resource 4', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294041', 4),
('DCSP', 'Distributed and Cloud System Programming', 3, 'Week 3 - Resource 5', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294042', 5),
('DCSP', 'Distributed and Cloud System Programming', 4, 'Week 4 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294043', 1),
('DCSP', 'Distributed and Cloud System Programming', 4, 'Week 4 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294044', 2),
('DCSP', 'Distributed and Cloud System Programming', 4, 'Week 4 - Resource 3', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294045', 3),
('DCSP', 'Distributed and Cloud System Programming', 4, 'Week 4 - Resource 4', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294047', 4),
('DCSP', 'Distributed and Cloud System Programming', 4, 'Week 4 - Resource 5', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294048', 5),
('DCSP', 'Distributed and Cloud System Programming', 4, 'Week 4 - Resource 6', 'https://canvas.wlv.ac.uk/courses/49700/modules/items/2294049', 6),

-- Databases
('DB', 'Databases', 1, 'Week 1 - Introduction', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384574', 1),
('DB', 'Databases', 2, 'Week 2 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384579', 1),
('DB', 'Databases', 2, 'Week 2 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384580', 2),
('DB', 'Databases', 3, 'Week 3 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384584', 1),
('DB', 'Databases', 3, 'Week 3 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384585', 2),
('DB', 'Databases', 4, 'Week 4 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384589', 1),
('DB', 'Databases', 4, 'Week 4 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384593', 2),
('DB', 'Databases', 5, 'Week 5 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384595', 1),
('DB', 'Databases', 5, 'Week 5 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384598', 2),
('DB', 'Databases', 6, 'Week 6 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384600', 1),
('DB', 'Databases', 6, 'Week 6 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49699/modules/items/2384602', 2),

-- Digital Forensics
('DF', 'Digital Forensics', 1, 'Week 1 - Introduction', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419159', 1),
('DF', 'Digital Forensics', 2, 'Week 2 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419163', 1),
('DF', 'Digital Forensics', 2, 'Week 2 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419164', 2),
('DF', 'Digital Forensics', 3, 'Week 3 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419170', 1),
('DF', 'Digital Forensics', 3, 'Week 3 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419171', 2),
('DF', 'Digital Forensics', 4, 'Week 4 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419181', 1),
('DF', 'Digital Forensics', 4, 'Week 4 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419182', 2),
('DF', 'Digital Forensics', 5, 'Week 5 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419187', 1),
('DF', 'Digital Forensics', 5, 'Week 5 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419188', 2),
('DF', 'Digital Forensics', 6, 'Week 6 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419190', 1),
('DF', 'Digital Forensics', 6, 'Week 6 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419191', 2),
('DF', 'Digital Forensics', 7, 'Week 7 - Resource 1', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419194', 1),
('DF', 'Digital Forensics', 7, 'Week 7 - Resource 2', 'https://canvas.wlv.ac.uk/courses/49703/modules/items/2419195', 2);
