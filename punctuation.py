#!/usr/bin/python3
# -*- coding: utf-8 -*-

code_point_threshold = 0x007F

current_char_code_point = 0x0021

rule_content = "{ "
while current_char_code_point < code_point_threshold:
    current_char = chr(current_char_code_point)
    if not current_char.isalpha() and not current_char.isdigit() and not current_char.isspace():
        rule_content += ("\"" + current_char + "\"")
        rule_content += " | "
    print("character={0}\ncode point={1}\n----------".format(current_char, current_char_code_point))
    current_char_code_point += 0x1
rule_content += ("\"" + chr(current_char_code_point) + "\"")
rule_content += " }"

rule_name = "punctuation"
rule = rule_name + " = " + rule_content

with open('markdown.pest', 'a', encoding='utf-8') as pest_file:
    pest_file.write('{0}\n'.format(rule))
