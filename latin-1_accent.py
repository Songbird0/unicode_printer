#!/usr/bin/python3
# -*- coding: utf-8 -*-

code_point_threshold = 0x00FF
current_char_code_point = (code_point_threshold - 0x0080) + 0x0022  # = 161

rule_content = "{ "
while current_char_code_point < code_point_threshold:
    current_char = chr(current_char_code_point)
    rule_content += ("\"" + current_char + "\"")
    rule_content += " | "
    current_char_code_point += 0x01
rule_content += ("\"" + chr(current_char_code_point) + "\"")
rule_content += " }"

rule_name = "accents"
rule = rule_name + " = " + rule_content

with open('markdown.pest', 'a', encoding='utf-8') as pest_file:
    pest_file.write('{0}\n'.format(rule))
