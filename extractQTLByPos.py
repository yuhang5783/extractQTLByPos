#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Description: extract QTL information using physical position of MSU reference genome
@Version: 0.01
@Author: Hang Yu
@Date: 2019-09-12 10:54:14
@LastEditTime: 2020-03-12 11:06:58
'''
import os

pos_file = "position.txt"
qtl_info_file = "qtlGeneInfoMSU6.txt"

qtl_pos_dict = {}
for qtl_info in open(qtl_info_file):
    qtl_name = qtl_info.split("\t")[0]
    qtl_chrom = qtl_info.split("\t")[1]
    qtl_start = qtl_info.split("\t")[2]
    qtl_end = qtl_info.split("\t")[3]
    qtl_pos_dict[qtl_name] = [qtl_chrom, qtl_start, qtl_end]

res_path = "result"
if not os.path.exists(res_path):
    os.mkdir(res_path)

var2qtl_name_file = open("result/pos_qtl_name.xls", "w")
qtl_name_list_total = []
for line in open(pos_file):
    qtl_name_list = []
    var_chrom = line.split()[0]
    var_pos = int(line.split()[1])
    for qtl_name in qtl_pos_dict.keys():
        qtl_chrom = qtl_pos_dict[qtl_name][0]
        qtl_start = int(qtl_pos_dict[qtl_name][1])
        qtl_end = int(qtl_pos_dict[qtl_name][2])
        if var_chrom == qtl_chrom \
        and var_pos >= qtl_start \
        and var_pos <= qtl_end:
            qtl_name_list.append(qtl_name)
    qtl_name_list_total += qtl_name_list

    var2qtl_name_file.write(var_chrom \
        + "\t" \
        + str(var_pos) \
        + "\t" \
        + "\t".join(qtl_name_list) \
        + "\n")
var2qtl_name_file.close()

qtl_name_set_total = set(qtl_name_list_total)
var_qtl_info = open("result/var_qtl_info.xls", "w")
for line in open(qtl_info_file):
    qtl_name = line.split("\t")[0]
    if qtl_name in qtl_name_set_total:
        var_qtl_info.write(line)
var_qtl_info.close()
