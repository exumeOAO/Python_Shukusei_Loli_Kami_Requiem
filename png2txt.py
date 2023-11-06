import numpy
from PIL import Image


# 将图片转换成灰度图
# 将图片分割成小块（自定义）
# 获取小块的长度、宽度等数值
# 计算相应的小块的灰度值
# 将灰度值对应的字符填入列表中
# 将列表导出为txt文件，查看结果


#  获取平均亮度
def getAverageLuminance(image):
    image_2 = numpy.array(image)
    width, height = image_2.shape
    average = numpy.average(image_2.reshape(height * width))
    return average


# 将图片转换成ascii文本
def ImageToAscii(file_name, str_i, cols=225, scale=0.225):  # 文件名，自定义列数，自定义缩放值
    # 定义灰度表
    gray_rank_70 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # 打开图片，将其转换为灰度图
    image_grey = Image.open(file_name).convert("L")
    # 获取图片的尺寸
    image_width, image_height = image_grey.size[0], image_grey.size[1]

    # 计算网格尺寸

    # 计算网格宽度
    w_tile = image_width / cols
    # 计算网格高度
    h_tile = w_tile / scale
    # 计算网格的行数
    rows_tile = int(image_height / h_tile)

    # 定义ascii字符串
    ascii_image = []

    # 遍历网格，计算灰度值，并且转换为ascii文本
    for j in range(rows_tile):
        y1 = int(j * h_tile)
        y2 = int((j + 1) * h_tile)
        ascii_image.append("")
        for i in range(cols):  # 自定义列数
            x1 = int(i * w_tile)
            x2 = int((i + 1) * w_tile)
            # 将这2*2图片在原灰度图中进行剪裁，并且计算灰度值：
            img = image_grey.crop((x1, y1, x2, y2))
            # 获取平均亮度
            avg = getAverageLuminance(img)
            # 在灰度表中寻找匹配的字符
            gray_scale_value = gray_rank_70[int((avg * 69) / 255)]
            ascii_image[j] += gray_scale_value

    # 将ascii文本保存
    with open(f"C:\\Users\\ASUS\\Desktop\\Python_Shukusei_Loli_Kami_Requiem\\alltxt\\{str_i}.txt", "w") as fp:
        for row in ascii_image:
            fp.write(row + "\n")
        fp.close()


# 运行
for i in range(1463):
    str_i = str(i + 10000)
    # str_i = '11127'
    ImageToAscii(f'C:\\Users\\ASUS\\Desktop\\Python_Shukusei_Loli_Kami_Requiem\\allpng\\{str_i}.png', str_i)
