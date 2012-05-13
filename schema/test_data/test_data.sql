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

REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 377150, -1224183);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (2, '2011-12-31 23:59:59', 377250, -1224283);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:59:59', 377350, -1224383);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:59:59', 377450, -1224483);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 23:59:59', 377550, -1224583);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 23:59:59', 377650, -1224683);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:59:59', 377750, -1224783);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:59:59', 377850, -1224883);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:59', 377950, -1224983);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 387050, -1214083);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:59:59', 387150, -1214183);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:59:59', 387250, -1214283);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 23:59:59', 387350, -1214383);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 23:59:59', 387450, -1214483);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:59:59', 387550, -1214583);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:59:59', 387650, -1214683);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:59', 387750, -1214783);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 367850, -1234883);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (2, '2011-12-31 23:59:59', 367950, -1234983);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:59:59', 367050, -1234183);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:59:59', 367150, -1234283);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 23:59:59', 367250, -1234383);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 23:59:59', 367350, -1234483);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:59:59', 367450, -1234583);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:59:59', 367550, -1234683);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:59', 367650, -1234783);

