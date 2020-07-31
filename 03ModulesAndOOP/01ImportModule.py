from PIL import Image
import sys

im = Image.open('test.png')
print(im.format, im.size, im.mode)
# 生成缩略图
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

# 当加载模块时
# Python解释器会搜索当前目录.所有已安装的内置模块和第三方模块
# 搜索路径存放在sys模块的path变量中
print(sys.path)

# 如果要添加自己的搜索目录
# 方法1
# sys.path.append('/Users/michael/my_py_scripts')
# 方法2
# 设置环境变量PYTHONPATH