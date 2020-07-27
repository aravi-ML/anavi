ALTER TABLE `comment_comment` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;

ALTER TABLE `comment_comment` CHANGE `text` `text` LONGTEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL, CHANGE `text_en` `text_en` LONGTEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL, CHANGE `text_fr` `text_fr` LONGTEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL, CHANGE `text_lang` `text_lang` VARCHAR(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

ALTER TABLE `comment_aspect` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `comment_aspecten` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `hotel_hotel` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `hotel_hotelwebsite` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `website_website` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `comment_polarity` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `auth_user` DEFAULT CHARSET=utf8 COLLATE utf8_unicode_ci;