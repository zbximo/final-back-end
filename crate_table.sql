CREATE TABLE `tb_content_group_user`  (
  `id` int NOT NULL,
  `group_user_id` int NULL,
  `keywords` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `create_datetime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '存储组内用户发言' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_content_person`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_app_person_id` int NOT NULL,
  `to_app_person_id` int NOT NULL,
  `keywords` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_bin NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `create_datetime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_bin COMMENT = '个人间不同应用的聊天记录' ROW_FORMAT = Dynamic;

CREATE TABLE `tb_info_app`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '应用表，包含微信、QQ、推特、电话等' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_app_person`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `app_id` int NOT NULL,
  `app_user_account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `app_user_nickname` varchar(255) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '由app_id和user_id组合，保存app_user_id，即APP用户账号。' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `group_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `app_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_group_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_person_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '用户和群' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `user_card_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_birthday` datetime NULL,
  `user_sex` varchar(255) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_sys_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `sys_user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `sys_user_pwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `sys_user_id` int NOT NULL,
  `sys_user_permision` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  PRIMARY KEY (`id`, `sys_user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '系统用户信息' ROW_FORMAT = DYNAMIC;

ALTER TABLE `tb_content_group_user` ADD CONSTRAINT `tb_content_group_user_ibfk_1` FOREIGN KEY (`group_user_id`) REFERENCES `tb_info_group_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `tb_content_person` ADD CONSTRAINT `tb_content_person_ibfk_1` FOREIGN KEY (`from_app_person_id`) REFERENCES `tb_info_app_person` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `tb_content_person` ADD CONSTRAINT `tb_content_person_ibfk_2` FOREIGN KEY (`to_app_person_id`) REFERENCES `tb_info_app_person` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `tb_info_app_person` ADD CONSTRAINT `fk_tb_info_app_person_tb_info_app_1` FOREIGN KEY (`app_id`) REFERENCES `tb_info_app` (`id`);
ALTER TABLE `tb_info_app_person` ADD CONSTRAINT `fk_tb_info_app_person_tb_info_user_1` FOREIGN KEY (`user_id`) REFERENCES `tb_info_user` (`id`);
ALTER TABLE `tb_info_group` ADD CONSTRAINT `fk_tb_info_group_tb_info_app_1` FOREIGN KEY (`app_id`) REFERENCES `tb_info_app` (`id`);
ALTER TABLE `tb_info_group_user` ADD CONSTRAINT `fk_tb_info_group_user_tb_info_app_person_1` FOREIGN KEY (`app_person_id`) REFERENCES `tb_info_app_person` (`id`);
ALTER TABLE `tb_info_group_user` ADD CONSTRAINT `fk_tb_info_group_user_tb_info_group_1` FOREIGN KEY (`group_id`) REFERENCES `tb_info_group` (`id`);

