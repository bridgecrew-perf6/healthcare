# Generated by Django 4.0.1 on 2022-01-15 10:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('dob', models.DateField(default=datetime.date(2022, 1, 15))),
                ('height', models.CharField(choices=[('43', '43 Cm'), ('44', '44 Cm'), ('45', '45 Cm'), ('46', '46 Cm'), ('47', '47 Cm'), ('48', '48 Cm'), ('49', '49 Cm'), ('50', '50 Cm'), ('51', '51 Cm'), ('52', '52 Cm'), ('53', '53 Cm'), ('54', '54 Cm'), ('55', '55 Cm'), ('56', '56 Cm'), ('57', '57 Cm'), ('58', '58 Cm'), ('59', '59 Cm'), ('60', '60 Cm'), ('61', '61 Cm'), ('62', '62 Cm'), ('63', '63 Cm'), ('64', '64 Cm'), ('65', '65 Cm'), ('66', '66 Cm'), ('67', '67 Cm'), ('68', '68 Cm'), ('69', '69 Cm'), ('70', '70 Cm'), ('71', '71 Cm'), ('72', '72 Cm'), ('73', '73 Cm'), ('74', '74 Cm'), ('75', '75 Cm'), ('76', '76 Cm'), ('77', '77 Cm'), ('78', '78 Cm'), ('79', '79 Cm'), ('80', '80 Cm'), ('81', '81 Cm'), ('82', '82 Cm'), ('83', '83 Cm'), ('84', '84 Cm'), ('85', '85 Cm'), ('86', '86 Cm'), ('87', '87 Cm'), ('88', '88 Cm'), ('89', '89 Cm'), ('90', '90 Cm'), ('91', '91 Cm'), ('92', '92 Cm'), ('93', '93 Cm'), ('94', '94 Cm'), ('95', '95 Cm'), ('96', '96 Cm'), ('97', '97 Cm'), ('98', '98 Cm'), ('99', '99 Cm'), ('100', '100 Cm'), ('101', '101 Cm'), ('102', '102 Cm'), ('103', '103 Cm'), ('104', '104 Cm'), ('105', '105 Cm'), ('106', '106 Cm'), ('107', '107 Cm'), ('108', '108 Cm'), ('109', '109 Cm'), ('110', '110 Cm'), ('111', '111 Cm'), ('112', '112 Cm'), ('113', '113 Cm'), ('114', '114 Cm'), ('115', '115 Cm'), ('116', '116 Cm'), ('117', '117 Cm'), ('118', '118 Cm'), ('119', '119 Cm'), ('120', '120 Cm'), ('121', '121 Cm'), ('122', '122 Cm'), ('123', '123 Cm'), ('124', '124 Cm'), ('125', '125 Cm'), ('126', '126 Cm'), ('127', '127 Cm'), ('128', '128 Cm'), ('129', '129 Cm'), ('130', '130 Cm'), ('131', '131 Cm'), ('132', '132 Cm'), ('133', '133 Cm'), ('134', '134 Cm'), ('135', '135 Cm'), ('136', '136 Cm'), ('137', '137 Cm'), ('138', '138 Cm'), ('139', '139 Cm'), ('140', '140 Cm'), ('141', '141 Cm'), ('142', '142 Cm'), ('143', '143 Cm'), ('144', '144 Cm'), ('145', '145 Cm'), ('146', '146 Cm'), ('147', '147 Cm'), ('148', '148 Cm'), ('149', '149 Cm'), ('150', '150 Cm'), ('151', '151 Cm'), ('152', '152 Cm'), ('153', '153 Cm'), ('154', '154 Cm'), ('155', '155 Cm'), ('156', '156 Cm'), ('157', '157 Cm'), ('158', '158 Cm'), ('159', '159 Cm'), ('160', '160 Cm'), ('161', '161 Cm'), ('162', '162 Cm'), ('163', '163 Cm'), ('164', '164 Cm'), ('165', '165 Cm'), ('166', '166 Cm'), ('167', '167 Cm'), ('168', '168 Cm'), ('169', '169 Cm'), ('170', '170 Cm'), ('171', '171 Cm'), ('172', '172 Cm'), ('173', '173 Cm'), ('174', '174 Cm'), ('175', '175 Cm'), ('176', '176 Cm'), ('177', '177 Cm'), ('178', '178 Cm'), ('179', '179 Cm'), ('180', '180 Cm'), ('181', '181 Cm'), ('182', '182 Cm'), ('183', '183 Cm'), ('184', '184 Cm'), ('185', '185 Cm'), ('186', '186 Cm'), ('187', '187 Cm'), ('188', '188 Cm'), ('189', '189 Cm'), ('190', '190 Cm'), ('191', '191 Cm'), ('192', '192 Cm'), ('193', '193 Cm'), ('194', '194 Cm'), ('195', '195 Cm'), ('196', '196 Cm'), ('197', '197 Cm'), ('198', '198 Cm'), ('199', '199 Cm')], max_length=5)),
                ('weight', models.CharField(choices=[('0', '0 Kg'), ('1', '1 Kg'), ('2', '2 Kg'), ('3', '3 Kg'), ('4', '4 Kg'), ('5', '5 Kg'), ('6', '6 Kg'), ('7', '7 Kg'), ('8', '8 Kg'), ('9', '9 Kg'), ('10', '10 Kg'), ('11', '11 Kg'), ('12', '12 Kg'), ('13', '13 Kg'), ('14', '14 Kg'), ('15', '15 Kg'), ('16', '16 Kg'), ('17', '17 Kg'), ('18', '18 Kg'), ('19', '19 Kg'), ('20', '20 Kg'), ('21', '21 Kg'), ('22', '22 Kg'), ('23', '23 Kg'), ('24', '24 Kg'), ('25', '25 Kg'), ('26', '26 Kg'), ('27', '27 Kg'), ('28', '28 Kg'), ('29', '29 Kg'), ('30', '30 Kg'), ('31', '31 Kg'), ('32', '32 Kg'), ('33', '33 Kg'), ('34', '34 Kg'), ('35', '35 Kg'), ('36', '36 Kg'), ('37', '37 Kg'), ('38', '38 Kg'), ('39', '39 Kg'), ('40', '40 Kg'), ('41', '41 Kg'), ('42', '42 Kg'), ('43', '43 Kg'), ('44', '44 Kg'), ('45', '45 Kg'), ('46', '46 Kg'), ('47', '47 Kg'), ('48', '48 Kg'), ('49', '49 Kg'), ('50', '50 Kg'), ('51', '51 Kg'), ('52', '52 Kg'), ('53', '53 Kg'), ('54', '54 Kg'), ('55', '55 Kg'), ('56', '56 Kg'), ('57', '57 Kg'), ('58', '58 Kg'), ('59', '59 Kg'), ('60', '60 Kg'), ('61', '61 Kg'), ('62', '62 Kg'), ('63', '63 Kg'), ('64', '64 Kg'), ('65', '65 Kg'), ('66', '66 Kg'), ('67', '67 Kg'), ('68', '68 Kg'), ('69', '69 Kg'), ('70', '70 Kg'), ('71', '71 Kg'), ('72', '72 Kg'), ('73', '73 Kg'), ('74', '74 Kg'), ('75', '75 Kg'), ('76', '76 Kg'), ('77', '77 Kg'), ('78', '78 Kg'), ('79', '79 Kg'), ('80', '80 Kg'), ('81', '81 Kg'), ('82', '82 Kg'), ('83', '83 Kg'), ('84', '84 Kg'), ('85', '85 Kg'), ('86', '86 Kg'), ('87', '87 Kg'), ('88', '88 Kg'), ('89', '89 Kg'), ('90', '90 Kg'), ('91', '91 Kg'), ('92', '92 Kg'), ('93', '93 Kg'), ('94', '94 Kg'), ('95', '95 Kg'), ('96', '96 Kg'), ('97', '97 Kg'), ('98', '98 Kg'), ('99', '99 Kg')], max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('emergency_contact', models.CharField(max_length=12)),
                ('current_doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
