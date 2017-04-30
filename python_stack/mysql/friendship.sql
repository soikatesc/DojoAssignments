-- use friendships
-- INSERT INTO 
-- INSERT INTO `friendships`.`users` (`id`, `first_name`,`last_name`,`created_at`,`updated_at`) VALUES ('4', 'jessica','davidson',now(),now());
select users.first_name, users.last_name, friend.first_name, friend.last_name from users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as friend ON friendships.friend_id = friend.id;

-- select * from friendships;
-- 
-- insert into friendships (user_id, friend_id, created_at, updated_at)
-- values (4, 1, now(), now());

-- select * from users; 

-- Total Revenue  =  Price  x  Quantity Sold