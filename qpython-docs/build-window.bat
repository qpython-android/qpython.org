@echo off
REM 删除 ../docs 目录
if exist ..\docs rmdir /s /q ..\docs

cd build/html

REM 使用 Python 执行 add-analytics.py 脚本
@REM for /r %%f in (*.html) do (
    python ..\..\add-analytics-window.py "%%f"
@REM )

REM 替换 _static 为 static，_images 为 images
for /r %%f in (*.html) do (
    echo Processing: %%f
    powershell -Command "(Get-Content '%%f' -Encoding UTF8) -replace '_static', 'static' | Set-Content '%%f' -Encoding UTF8"
    powershell -Command "(Get-Content '%%f' -Encoding UTF8) -replace '_images', 'images' | Set-Content '%%f' -Encoding UTF8"
)

REM 删除临时文件
for /r %%f in (*-e) do (
    del "%%f"
)

REM 重命名 _static 为 static，_images 为 images
ren _static static
ren _images images

REM 返回上级目录
cd ..\..

REM 将 build/html 移动到 ../docs
move build\html ..\docs

REM 复制其他文件到 ../docs
copy CNAME ..\docs
xcopy quick-start ..\docs /s /e
copy favicon.ico ..\docs
copy index.html ..\docs
copy community.html ..\docs
copy discord.html ..\docs
copy privacy.html ..\docs
copy privacy-cn.html ..\docs
copy agreement-cn.html ..\docs
copy agreement.html ..\docs
copy qlua-privacy.html ..\docs
copy qlua-rate.html ..\docs
copy qpy3-rate.html ..\docs
xcopy market ..\docs /s /e

echo 部署完成！