:: StickyBoard 打包助手
chcp 65001
@echo off  
setlocal enabledelayedexpansion  
  
set "version=1.0"  
set "buildForWindows=pyinstaller -F -w -i icon.ico main.py"  
  
echo StickyBoard 打包助手  
echo 版本：%version%  
  
echo.  
echo 请选择构建目标：  
echo 1. 为Windows构建  
echo 2. 为Gnome Linux构建 (敬请期待)  
echo 3. 为KDE Linux构建 (敬请期待)  
echo.  
  
:input_loop  
set /p "prompt=请输入序号 (1-3): "  
if "!prompt!"=="1" goto :build_windows  
if "!prompt!"=="2" goto :build_gnome  
if "!prompt!"=="3" goto :build_kde  
echo 输入序号错误，请重新输入。  
goto :input_loop  
  
:build_windows  
echo 正在为Windows构建...  
%buildForWindows%  
goto :end  
  
:build_gnome  
echo 敬请期待。  
goto :end  
  
:build_kde  
echo 敬请期待。  
goto :end  
  
:end  
echo.  
echo 完成。  
pause  
endlocal