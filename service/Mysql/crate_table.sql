CREATE TABLE `tb_content_group_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_user_id` int NULL,
  `keywords` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `record_datetime` datetime NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '存储组内用户发言' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_content_personal`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_app_user_id` int NOT NULL,
  `to_app_user_id` int NOT NULL,
  `keywords` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `record_datetime` datetime NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_bin COMMENT = '个人间不同应用的聊天记录' ROW_FORMAT = Dynamic;

CREATE TABLE `tb_info_app`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '应用表，包含微信、QQ、推特、电话等' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_app_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `app_id` int NOT NULL,
  `app_user_account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `app_user_nickname` varchar(255) NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '由app_id和user_id组合，保存app_user_id，即APP用户账号。' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `group_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `app_id` int NOT NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_group_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_user_id` int NOT NULL,
  `group_id` int NOT NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '用户和群' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_telephone`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `telephone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_info_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `card_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `birthday` date NULL,
  `sex` varchar(255) NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_sys_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `pwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `account` int NOT NULL,
  `permission_id` int NULL DEFAULT NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`, `account`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '系统用户信息' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_sys_user_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `permission` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '用户权限表' ROW_FORMAT = DYNAMIC;

CREATE TABLE `tb_telephone_record`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_telephone_id` int NOT NULL,
  `to_telephone_id` int NOT NULL,
  `record_datetime` datetime NULL,
  `create_datetime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '个人间电话记录' ROW_FORMAT = Dynamic;

ALTER TABLE `tb_content_group_user` ADD CONSTRAINT `tb_content_group_user_ibfk_1` FOREIGN KEY (`group_user_id`) REFERENCES `tb_info_group_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `tb_content_personal` ADD CONSTRAINT `tb_content_person_ibfk_1` FOREIGN KEY (`from_app_user_id`) REFERENCES `tb_info_app_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `tb_content_personal` ADD CONSTRAINT `tb_content_person_ibfk_2` FOREIGN KEY (`to_app_user_id`) REFERENCES `tb_info_app_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `tb_info_app_user` ADD CONSTRAINT `fk_tb_info_app_user_tb_info_app_1` FOREIGN KEY (`app_id`) REFERENCES `tb_info_app` (`id`);
ALTER TABLE `tb_info_app_user` ADD CONSTRAINT `fk_tb_info_app_user_tb_info_user_1` FOREIGN KEY (`user_id`) REFERENCES `tb_info_user` (`id`);
ALTER TABLE `tb_info_group` ADD CONSTRAINT `fk_tb_info_group_tb_info_app_1` FOREIGN KEY (`app_id`) REFERENCES `tb_info_app` (`id`);
ALTER TABLE `tb_info_group_user` ADD CONSTRAINT `fk_tb_info_group_user_tb_info_app_user_1` FOREIGN KEY (`app_user_id`) REFERENCES `tb_info_app_user` (`id`);
ALTER TABLE `tb_info_group_user` ADD CONSTRAINT `fk_tb_info_group_user_tb_info_group_1` FOREIGN KEY (`group_id`) REFERENCES `tb_info_group` (`id`);
ALTER TABLE `tb_info_telephone` ADD CONSTRAINT `fk_tb_info_telephone_tb_info_user_1` FOREIGN KEY (`user_id`) REFERENCES `tb_info_user` (`id`);
ALTER TABLE `tb_sys_user` ADD CONSTRAINT `fk_tb_sys_user_tb_sys_user_permission_1` FOREIGN KEY (`permission_id`) REFERENCES `tb_sys_user_permission` (`id`);
ALTER TABLE `tb_telephone_record` ADD CONSTRAINT `fk_tb_telephone_record_tb_info_telephone_1` FOREIGN KEY (`from_telephone_id`) REFERENCES `tb_info_telephone` (`id`);
ALTER TABLE `tb_telephone_record` ADD CONSTRAINT `fk_tb_telephone_record_tb_info_telephone_2` FOREIGN KEY (`to_telephone_id`) REFERENCES `tb_info_telephone` (`id`);

