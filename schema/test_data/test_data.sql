#Category seed 

REPLACE INTO category (name) VALUES ('mexican');
REPLACE INTO category (name) VALUES ('chinese');
REPLACE INTO category (name) VALUES ('thai');
REPLACE INTO category (name) VALUES ('korean');
REPLACE INTO category (name) VALUES ('italian');
REPLACE INTO category (name) VALUES ('bbq');
REPLACE INTO category (name) VALUES ('grilled_cheese');
REPLACE INTO category (name) VALUES ('fusions');
REPLACE INTO category (name) VALUES ('american');
REPLACE INTO category (name) VALUES ('filipino');
REPLACE INTO category (name) VALUES ('dessert');
REPLACE INTO category (name) VALUES ('indian');
REPLACE INTO category (name) VALUES ('breakfast');
REPLACE INTO category (name) VALUES ('vietnamese');
REPLACE INTO category (name) VALUES ('juice');
REPLACE INTO category (name) VALUES ('french');


#Entity seed 

REPLACE INTO entity (name, categorynode_id) VALUES ('adobo_hobo', 10);
REPLACE INTO entity (name, categorynode_id) VALUES ('chairman_truck', 2);
REPLACE INTO entity (name, categorynode_id) VALUES ('creme_brulee_cart', 11);
REPLACE INTO entity (name, categorynode_id) VALUES ('crepes_a_gogo', 11);
REPLACE INTO entity (name, categorynode_id) VALUES ('cup_kates_truck', 11);
REPLACE INTO entity (name, categorynode_id) VALUES ('curry_up_now', 12);
REPLACE INTO entity (name, categorynode_id) VALUES ('el_porteno_empanadas', 1);
REPLACE INTO entity (name, categorynode_id) VALUES ('magic_curry_man', 12);
REPLACE INTO entity (name, categorynode_id) VALUES ('amuse_bouche_sf', 13);
REPLACE INTO entity (name, categorynode_id) VALUES ('mobile_pho_truck', 14);
REPLACE INTO entity (name, categorynode_id) VALUES ('urban_nectar', 15);
REPLACE INTO entity (name, categorynode_id) VALUES ('spencer_on_the_go', 16);
REPLACE INTO entity (name, categorynode_id) VALUES ('roli_roti', 12);
REPLACE INTO entity (name, categorynode_id) VALUES ('cookie_wag_sf', 11);
REPLACE INTO entity (name, categorynode_id) VALUES ('the_tamale_lady', 1);
REPLACE INTO entity (name, categorynode_id) VALUES ('left_coast_smoke', 6);

#Entity instance seed

REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 377150, -1224183);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (2, '2011-12-01 23:59:59', 377250, -1224283);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-21 23:59:59', 377350, -1224383);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-22 23:59:59', 377450, -1224483);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 22:59:59', 377550, -1224583);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 21:59:59', 377650, -1224683);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 20:59:59', 377750, -1224783);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-30 23:59:59', 377850, -1224883);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-29 23:59:59', 377950, -1224983);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (1, '2011-12-31 23:59:59', 387050, -1214083);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (3, '2011-12-31 23:39:59', 387150, -1214183);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (4, '2011-12-31 23:29:59', 387250, -1214283);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (5, '2011-12-31 12:59:59', 387350, -1214383);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (6, '2011-12-31 14:59:59', 387450, -1214483);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 20:59:59', 387550, -1214583);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 15:59:59', 387650, -1214683);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:59:50', 387750, -1214783);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (11, '2011-12-31 23:59:51', 367850, -1234883);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (12, '2011-12-31 23:59:52', 367950, -1234983);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (13, '2011-12-31 23:59:53', 367050, -1234183);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (14, '2011-12-31 23:50:59', 367150, -1234283);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (15, '2011-12-31 23:51:59', 367250, -1234383);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (16, '2011-12-31 23:52:59', 367350, -1234483);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (7, '2011-12-31 23:53:59', 367450, -1234583);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (8, '2011-12-31 23:54:59', 367550, -1234683);
REPLACE INTO entityinstance (entitynode_id, time_instance, latitude, longitude) VALUES (9, '2011-12-31 23:55:59', 367650, -1234783);

#Social Network seed

REPLACE INTO socialnetwork (social_network) VALUES ('facebook');
REPLACE INTO socialnetwork (social_network) VALUES ('twitter');
REPLACE INTO socialnetwork (social_network) VALUES ('foursquare');

#Social Network Data seed

REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (1, 2, '59991967', 'adobohobo');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (2, 2, '136865608', 'chairmantruck');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (3, 2, '25612932', 'cremebruleecart');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (4, 2, '43835812', 'crepesagogo');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (5, 2, '45983922', 'cupkatestruck');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (6, 2, '68867011', 'curryupnow');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (7, 2, '63405234', 'elporteno');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (8, 2, '23233081', 'magiccurrykart');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (9, 2, '28742966', 'amusebouchesf');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (10, 2, '27547864', 'whatthepho');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (11, 2, '68150676', 'urbannectar');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (12, 2, '36159715', 'chezspencergo');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (13, 2, '32143933', 'roliroti');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (14, 2, '38622430', 'cookiewagsf');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (15, 2, '40296757', 'tamalelady');
REPLACE INTO socialnetworkdata (entitynode_id, social_network_node_id, network_id, handle) VALUES (16, 2, '38705804', 'leftcoastsmoke');
