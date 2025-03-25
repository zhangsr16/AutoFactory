import xlrd, sys, os, re

input_file = "./excel_list"
outfile_py = "lp_flow.py"
remark = "### start\n"


def check_struck_out(ExcelFile, work_sheet, rows, cols):
    xf = ExcelFile.xf_list[work_sheet.cell_xf_index(rows, cols)]
    font = ExcelFile.font_list[xf.font_index]
    if font.struck_out:
        return True
    else:
        return False


xls_File = open(input_file, 'r')
xls_List = xls_File.readlines()

# --------------------------------------------------
# Generate output files
# --------------------------------------------------
# {{{
fid_out_py = open(outfile_py, "w+")
fid_out_py.write(remark + "\n")
fid_out_py.write('import numpy\n')
for xls_idx in range(len(xls_List)):
    ExcelFile = xlrd.open_workbook(xls_List[xls_idx].strip(), formatting_info=True)
    all_sheets = ExcelFile.sheet_names()
    print("Info: Parser excel: %s!" % xls_List[xls_idx])
    for sht_idx in range(len(all_sheets)):
        if (re.match("^set_", all_sheets[sht_idx]) != None):  # read set_*.sheet
            print("Info: Parser sheet: %s!" % all_sheets[sht_idx])
            work_sheet = ExcelFile.sheet_by_index(sht_idx)
            # Generate func_name list
            func_name_l = []
            func_name_l.append(work_sheet.name)
            func_list = func_name_l
            multi_func_flag = 0
            # Generate output files
            fid_out_py.write("\ndef " + work_sheet.name + "():\n")
            fid_out_py.write("\tprint(\"Begin " + work_sheet.name + "\\n\") \n")
            explain_flag = 0
            for row_idx in range(work_sheet.nrows):
                special_cell = 0
                cell_step = work_sheet.cell_value(row_idx, 0)
                cell_reg_base = work_sheet.cell_value(row_idx, 1)
                cell_reg_name = work_sheet.cell_value(row_idx, 2)
                cell_reg_offset = work_sheet.cell_value(row_idx, 3)
                cell_op_code = work_sheet.cell_value(row_idx, 4)
                cell_member = work_sheet.cell_value(row_idx, 5)
                cell_bit_range = work_sheet.cell_value(row_idx, 6)
                cell_wr_val = work_sheet.cell_value(row_idx, 7)
                cell_rd_val = work_sheet.cell_value(row_idx, 8)
                cell_wait = work_sheet.cell_value(row_idx, 9).replace(" ", "")
                # --------------------------------------------------
                # Parser StepIndex and StepExplain in merge cell
                # --------------------------------------------------
                for (rlow, rhigh, clow, chigh) in work_sheet.merged_cells:
                    if (clow == 0) and (chigh == 1) and (rhigh - rlow > 1) and (row_idx >= rlow) and (
                            row_idx < rhigh):  # StepIndex
                        if (cell_step != "") and (check_struck_out(ExcelFile, work_sheet, row_idx, 0) == False):
                            fid_out_py.write("\t## " + cell_step + "\n")
                            special_cell = 1
                    if (clow == 1) and (chigh > 11) and (rhigh - rlow == 1) and (row_idx >= rlow) and (
                            row_idx < rhigh):  # StepExplain from col=1
                        explain_flag = explain_flag + 1
                        if (cell_reg_base != "") and (explain_flag % 2 == 0) and (
                                check_struck_out(ExcelFile, work_sheet, row_idx, 1) == False):
                            fid_out_py.write("\t## " + cell_reg_base + "\n")
                            special_cell = 2
                            break
                    if (clow == 2) and (chigh > 11) and (rhigh - rlow == 1) and (row_idx >= rlow) and (
                            row_idx < rhigh):  # StepExplain from col=2
                        explain_flag = explain_flag + 1
                        if (cell_reg_name != "") and (explain_flag % 2 == 0) and (
                                check_struck_out(ExcelFile, work_sheet, row_idx, 2) == False):
                            fid_out_py.write("\t## " + cell_reg_name + "\n")
                            special_cell = 2
                            break

                if (special_cell == 1):
                    continue
                elif (check_struck_out(ExcelFile, work_sheet, row_idx, 4) == False):  ##option in col=4
                    print_mode = "PRINT";
                    head_str_l = []
                    tail_str_l = []

                    # --------------------------------------------------
                    # Print to output c_file
                    # --------------------------------------------------
                    if (len(head_str_l) != 0):
                        for idx in range(len(head_str_l)):
                            fid_out_py.write(head_str_l[idx] + "\n")
                    if (len(tail_str_l) != 0):
                        for idx in range(len(tail_str_l)):
                            fid_out_py.write(tail_str_l[idx] + "\n")
            fid_out_py.write("\tprint(\"End " + work_sheet.name + "\\n\") \n")
            fid_out_py.write("\treturn 1\n")
            fid_out_py.write("\n")
# }}}
