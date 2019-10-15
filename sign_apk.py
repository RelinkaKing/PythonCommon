import sys,os
if len(sys.argv) !=3:
    print('params count error ')
else:
    file_name=sys.argv[1]
    zipalign_name=file_name.split('.apk')[0]+'_zipalign.apk'
    command='zipalign -v -p 4 {0} {1}'.format(file_name,zipalign_name)
    os.system(command)
    jks_name=zipalign_name.split('.apk')[0]+'_signed.apk'
    commad='apksigner sign --ks {0} --out {1} {2}'.format(jks_name,apk_name,zipalign_name)
    os.system(commad)
# bat 命令
# 25.0.2  sdk\build-tools
# 4子节对齐
#   491  ./zipalign.exe -v -p 4 D:/Vesal/LEGUPC-WINDOWS-V2.0.7/output/app-yingyongbao-release_legu.apk D:/Vesal/LEGUPC-WINDOWS-V2.0.7/output/app-yingyongbao-release_legu_align.apk
#   497  cd lib
# 签名
#   499  java -jar apksigner.jar sign --ks D:/Vesal/LEGUPC-WINDOWS-V2.0.7/signfile/Vesal.jks --ks-key-alias hello --ks-pass pass:softeasy --key-pass pass:softeasy --out output.apk D:/Vesal/LEGUPC-WINDOWS-V2.0.7/output/app-yingyongbao-release_legu_align.apk
# 检查签名是否成功
#   500  java -jar apksigner.jar verify -v output.apk