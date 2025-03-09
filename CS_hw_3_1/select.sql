-- Отримати всі завдання певного користувача.
SELECT *
FROM tasks
WHERE user_id = 3;

-- Вибрати завдання за певним статусом.
SELECT *
FROM tasks
WHERE status = (SELECT 'new' AS status); 

-- Оновити статус конкретного завдання. 
UPDATE tasks
SET status = 'in progress'
WHERE task_id = 5;

-- Отримати список користувачів, які не мають жодного завдання. 
SELECT *
FROM users
WHERE user_id NOT IN (SELECT user_id FROM tasks); 

-- Додати нове завдання для конкретного користувача.
INSERT INTO tasks (title, description, user_id)
VALUES ('update database', 'use new data from last day', 3);

-- Отримати всі завдання, які ще не завершено. 
SELECT *
FROM tasks
WHERE status NOT IN (SELECT status FROM tasks WHERE status = "completed");

-- Видалити конкретне завдання. 
DELETE FROM tasks
WHERE task_id = 3;

-- Знайти користувачів з певною електронною поштою. 
SELECT *
FROM users
WHERE email LIKE 'mail@gmail.com';

-- Оновити ім'я користувача. 
UPDATE users
SET name = 'João'
WHERE user_id = '4';

-- Отримати кількість завдань для кожного статусу. 
SELECT status, COUNT(*) AS task_count
FROM tasks
GROUP BY status;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. 
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.user_id
WHERE users.email LIKE '%@example.com';

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT *
FROM tasks
WHERE description IS NULL;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 
SELECT users.user_id, users.name, users.email, tasks.task_id, tasks.title, tasks.status
FROM users
INNER JOIN tasks ON users.user_id = tasks.user_id
WHERE tasks.status = 'in progress';

-- Отримати користувачів та кількість їхніх завдань. 
SELECT users.user_id, users.name, users.email, COUNT(tasks.task_id) AS task_count
FROM users
LEFT JOIN tasks ON users.user_id = tasks.user_id
GROUP BY users.user_id, users.name, users.email;
