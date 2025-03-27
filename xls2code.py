import re
from openpyxl import load_workbook

outfile_py = "outCode.py"
remark = "### start\n"
xls_File = open("./excel_list", 'r')
xls_List = xls_File.readlines()

# --------------------------------------------------
# Generate output files
# --------------------------------------------------
# {{{
fid_out_py = open(outfile_py, "w+")
fid_out_py.write(remark + "\n")
fid_out_py.write('import numpy\n')
for xls_idx in range(len(xls_List)):
    ExcelFile = load_workbook(xls_List[xls_idx].strip())
    all_sheets = ExcelFile.sheetnames
    print("Info: Parser excel: %s!" % xls_List[xls_idx])
    for sht_idx in range(len(all_sheets)):
        row_start = 2
        col_start = 1
        if (re.match("^Expect_", all_sheets[sht_idx]) != None):  # read set_*.sheet
            print("Info: Parser sheet: %s!" % all_sheets[sht_idx])
            work_sheet = ExcelFile.worksheets[sht_idx]
            cell_expectation = work_sheet.cell(row=row_start, column=col_start).value
            row_start += 1
            col_start += 1
            # Generate output files
            fid_out_py.write("\ndef " + work_sheet.title + "():\n")
            fid_out_py.write("\tprint(\"" + cell_expectation + "\\n\") \n")
            for row_idx in range(work_sheet.max_row):
                cell_step = work_sheet.cell(row=row_start, column=col_start).value
                if cell_step == None:
                    break
                if cell_step == '步骤':
                    row_start += 1
                    col_start += 1
                elif "&&&&" in cell_step:
                    row_start += 1
                else:
                    row_start += 1
                    col_start -= 1
                fid_out_py.write("\tprint(\"" + cell_step + "\\n\") \n")

            fid_out_py.write("\tprint(\"End " + work_sheet.title + "\\n\") \n")
            fid_out_py.write("\treturn 1\n")
            fid_out_py.write("\n")
# }}}
