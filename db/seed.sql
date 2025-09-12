-- Default Events
-- Default Events (simplified schema, no points)
INSERT INTO Events (name) VALUES
('Chess'),
('Cyquest'),
('Dexterity'),
('Digital Imaging'),
('Fotographia'),
('24 Frames'),
('Programming'),
('Quiz'),
('Respawn Console'),
('Respawn Mobile'),
('Respawn PC'),
('Robowars'),
('Surprise'),
('Verse Off');

-- Default Schools
INSERT INTO Schools (name) VALUES
('Amity International School, Mayur Vihar'),
('Ahlcon Public School, Mayur Vihar'),
('Delhi Public School, R.K. Puram'),
('Delhi Public School, Vasant Kunj'),
('Modern School, Barakhamba Road'),
('Springdales School, Dhaula Kuan'),
('The Shri Ram School, Aravali'),
('Sardar Patel Vidyalaya'),
('Mayoor School, Noida'),
('Somerville School, Noida');

-- Note: A default 'admin' user is created by the application automatically.
-- No need to insert users here.

-- Sample Results
INSERT INTO Results (event_id, first_place_school, second_place_school, third_place_school, submitted_at) VALUES
(1, 'Amity International School, Mayur Vihar', 'Delhi Public School, R.K. Puram', 'Modern School, Barakhamba Road', '2025-08-23 09:00:00'),
(2, 'Delhi Public School, Vasant Kunj', 'Ahlcon Public School, Mayur Vihar', 'Springdales School, Dhaula Kuan', '2025-08-23 09:05:00'),
(3, 'The Shri Ram School, Aravali', 'Sardar Patel Vidyalaya', 'Mayoor School, Noida', '2025-08-23 09:10:00');

-- Update results_entered flag for seeded events
UPDATE Events SET results_entered = 1 WHERE id IN (1, 2, 3);
