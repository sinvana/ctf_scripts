import hashlib
demo = input("请输入要md5加密的值：")
md5 = hashlib.md5()
md5.update(demo.encode("utf-8"))
print(md5.hexdigest())
input("...")
