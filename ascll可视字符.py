import hashlib

a = "38e4c352809e150186920aac37190cbc"
dic = "0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
dic8 = "@8Mu1"
i=0
for i1 in dic:
    for i2 in dic:
        for i3 in dic:
            for i4 in dic:
                str = "flag{www_shiyanbar_com_is_very_good_"+i1+i2+i3+i4+"}"
                md5 = hashlib.md5()
                md5.update(str.encode("utf-8"))
                m = md5.hexdigest()
                i = i+1
                print(m,"\t",i)
                if m==a:
                    print(str)
                    input("...")

        
#flag{www_shiyanbar_com_is_very_good_@8Mu}
