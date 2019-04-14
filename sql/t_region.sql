/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50624
 Source Host           : localhost:3306
 Source Schema         : local_db

 Target Server Type    : MySQL
 Target Server Version : 50624
 File Encoding         : 65001

 Date: 14/04/2019 21:48:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_region
-- ----------------------------
DROP TABLE IF EXISTS `t_region`;
CREATE TABLE `t_region`  (
  `T_REGION_CODE` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `T_REGION_NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `T_REGION_DISABLED` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `T_REGION_ALIAS` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '别名',
  `T_REGINALIZATION` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_region
-- ----------------------------
INSERT INTO `t_region` VALUES ('cn-qingdao-cm5-a01', '华北 1', '0', 'cn-qingdao', '0');
INSERT INTO `t_region` VALUES ('cn-beijing-btc-a01', '华北 2', '0', 'cn-beijing', '0');
INSERT INTO `t_region` VALUES ('cn-zhangjiakou-na62-a01', '华北 3', '0', 'cn-zhangjiakou', '1');
INSERT INTO `t_region` VALUES ('cn-huhehaote-nt12-a01', '华北 5', '0', 'cn-huhehaote', '1');
INSERT INTO `t_region` VALUES ('cn-hangzhou-dg-a01', '华东 1', '0', 'cn-hangzhou', '0');
INSERT INTO `t_region` VALUES ('cn-shanghai-eu13-a01', '华东 2', '0', 'cn-shanghai', '0');
INSERT INTO `t_region` VALUES ('cn-shenzhen-st3-a01', '华南 1', '0', 'cn-shenzhen', '0');
INSERT INTO `t_region` VALUES ('cn-hongkong-am4-c04', '香港', '0', 'cn-hongkong', '0');
INSERT INTO `t_region` VALUES ('ap-southeast-os30-a01', '亚太东南 1 (新加坡)', '0', 'ap-southeast-1', '0');
INSERT INTO `t_region` VALUES ('us-west-ot7-a01', '美国西部 1 (硅谷)', '0', 'us-west-1', '0');
INSERT INTO `t_region` VALUES ('us-east-us44-a01', '美国东部 1 (弗吉尼亚)', '0', 'us-east-1', '0');
INSERT INTO `t_region` VALUES ('ap-northeast-jp59-a01', '亚太东北 1 (东京)', '0', 'ap-northeast-1', '1');
INSERT INTO `t_region` VALUES ('eu-central-de46-a01', '欧洲中部 1 (法兰克福)', '0', 'eu-central-1', '1');
INSERT INTO `t_region` VALUES ('me-east-db47-a01', '中东东部 1 (迪拜)', '0', 'me-east-1', '1');
INSERT INTO `t_region` VALUES ('ap-southeast-au49-a01', '亚太东南 2 (悉尼)', '0', 'ap-southeast-2', '1');
INSERT INTO `t_region` VALUES ('ap-southeast-my88-a01', '亚太东南 3 (吉隆坡)', '0', 'ap-southeast-3', '1');
INSERT INTO `t_region` VALUES ('ap-south-in73-a01', '亚太南部 1 (孟买)', '0', 'ap-south-1', '1');
INSERT INTO `t_region` VALUES ('ap-southeast-id35-a01', '亚太东南 5 (雅加达)', '0', 'ap-southeast-5', '1');
INSERT INTO `t_region` VALUES ('eu-west-1-gb33-a01', '英国', '0', 'eu-west-1', '1');

SET FOREIGN_KEY_CHECKS = 1;
