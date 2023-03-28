# pip install paddlepaddle-gpu
# pip install paddleocr


from paddleocr import PaddleOCR,draw_ocr 
#####################
import os
import matplotlib.pyplot as plt
import glob
# %matplotlib inline
import cv2
ocr = PaddleOCR(use_angle_cls=True)

# result = ocr.ocr(img_path)
# print("======================")
out_path = 'D:\\lincode\\paddle_ocr\\out\\'
font = "D:\\lincode\\paddle_ocr\\font\\simfang.ttf"

# img_path = "C:\\Users\\jebar\\OneDrive\\Desktop\\bidi-ocr\\image0000140.jpg"
# images = 'C:\\Users\\jebar\\OneDrive\\Desktop\\paddleocr\\*.jpg'
images = glob.glob('D:\\lincode\\paddle_ocr\\*.jpg')
print("\n\n\nredddddddddddddddddddd1",images)

count = 0
for x in images:
    count = count+1

    result = ocr.ocr(x)




    def save_ocr(img_path, out_path, result, font):

        save_path = os.path.join(out_path, img_path.split('/')[-1] + 'output')
        print("save_path>>>>>>>>>>>>>>>>>>>>>>>>",save_path)

        image = cv2.imread(img_path)
        print("redddddddddddddddddddd2",img_path)
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        print(txts)

        im_show = draw_ocr(image, boxes, txts, scores, font_path=font)
        print("redddddddddddddddddddd3",img_path)
        # cv2.imwrite(save_path, im_show)
        cv2.imwrite(str(count)+"_CM.jpg", im_show)

        img = cv2.cvtColor(im_show, cv2.COLOR_BGR2RGB)
        plt.imshow(img)

    for result in result:
        result = result
        save_ocr(x, out_path, result, font)
