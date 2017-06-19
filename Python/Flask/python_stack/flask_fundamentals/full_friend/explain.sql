SELECT curr_user.id AS user_id, CONCAT(curr_user.first_name, ' ', curr_user.last_name) AS user_name, curr_user.email AS request_email, friend_user.id AS friends_id, CONCAT(friend_user.first_name, ' ', friend_user.last_name) AS friend_name, friend_user.email AS friend_email
FROM users AS curr_user 
LEFT JOIN friendships as f ON curr_user.id = f.user_id 
LEFT JOIN users AS friend_user ON  f.friend_id = friend_user.id
WHERE f.user_id = 10 or f.friend_id = 10;
