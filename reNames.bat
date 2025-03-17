@echo off
setlocal enabledelayedexpansion

rem 定义文件名前缀
set prefix=2_

rem 获取当前目录下的所有xlsx文件
for %%f in (*.xlsx) do (
    rem 构造新文件名
    set newname=!prefix!%%f
    rem 重命名文件
    ren "%%f" "!newname!"
)

endlocal
