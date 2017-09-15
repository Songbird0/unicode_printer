#!/usr/bin/python3
# -*- coding: utf-8 -*-

def build_to_pest_rule( rule_name, code_point_list ):
    rule_content = '{' + chr(0x0020)
    accumulator = 0
    code_point_list_length = len(code_point_list)
    while accumulator < code_point_list_length - 1:
        current_code_point = code_point_list[accumulator]
        character = chr(current_code_point)
        rule_content += '"' + character + '"' + chr(0x0020) + '|' + chr(0x0020)
        accumulator += 1
    last_code_point = code_point_list[accumulator]
    character = chr(last_code_point)
    rule_content += '"' + character + '"' + chr(0x0020) + '}'
    rule = rule_name + chr(0x0020) + '=' + chr(0x0020) + rule_content
    return rule
