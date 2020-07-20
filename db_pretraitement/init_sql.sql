ALTER TABLE `comment_comment` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;

ALTER TABLE `comment_comment` CHANGE `text` `text` LONGTEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL, CHANGE `text_en` `text_en` LONGTEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL, CHANGE `text_fr` `text_fr` LONGTEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL, CHANGE `text_lang` `text_lang` VARCHAR(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

