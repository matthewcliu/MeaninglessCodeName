#Category seed data

REPLACE INTO category (name) VALUES ('mexican');
REPLACE INTO category (name) VALUES ('chinese');
REPLACE INTO category (name) VALUES ('thai');
REPLACE INTO category (name) VALUES ('korean');
REPLACE INTO category (name) VALUES ('italian');
REPLACE INTO category (name) VALUES ('bbq');
REPLACE INTO category (name) VALUES ('grilled_cheese');
REPLACE INTO category (name) VALUES ('fusions');
REPLACE INTO category (name) VALUES ('american');

#Entity seed data

REPLACE INTO entity (name, categorynode_id) VALUES ('san_jose_tacos', 1);
REPLACE INTO entity (name, categorynode_id) VALUES ('bobs_tacos', 1);
REPLACE INTO entity (name, categorynode_id) VALUES ('siesta_fiesta', 1);
REPLACE INTO entity (name, categorynode_id) VALUES ('wong_fu_lee', 2);
REPLACE INTO entity (name, categorynode_id) VALUES ('bok_choy', 2);
REPLACE INTO entity (name, categorynode_id) VALUES ('goldman_chinese', 2);
REPLACE INTO entity (name, categorynode_id) VALUES ('saureen_szechuan', 2);
REPLACE INTO entity (name, categorynode_id) VALUES ('thai_tran', 3);
REPLACE INTO entity (name, categorynode_id) VALUES ('tranny_thai', 3);
REPLACE INTO entity (name, categorynode_id) VALUES ('pad_thai_plus', 3);
REPLACE INTO entity (name, categorynode_id) VALUES ('pad_thai_small', 3);
REPLACE INTO entity (name, categorynode_id) VALUES ('pad_thai_medium', 3);
REPLACE INTO entity (name, categorynode_id) VALUES ('pad_see_ew', 3);
REPLACE INTO entity (name, categorynode_id) VALUES ('ginger_chicken', 3);

#Entity instance data

REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (2, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:59', 123445566, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:59', 222222222, 123445566);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (2, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:59:59', 123445566, 222222222);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:59', 123445566, 222222222);

