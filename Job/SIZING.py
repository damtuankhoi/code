import glob
import json
import cv2
import math

folder_path = r'F:/SIZING/2022-07-24/*.json'
index_count = 0
sum = 0
blue_count = 0
white_count = 0
for file in glob.glob(folder_path, recursive=True):
    print(file)

    with open(file, 'r') as f:  
        data = json.load(f)
        total = len(data)
        type_arr = [item['skeleton_type'] for item in data]

        arr_bbox_missing_joints = [item['bbox'] for item in data if item['skeleton_type'] == 'Missing joints']
        print('bbox_missing_joints:', arr_bbox_missing_joints)
        img = cv2.imread(file.replace('.pred.json', '.jpeg'))

        for item in arr_bbox_missing_joints:

            try:
                imgCropped = img[item[1]:item[3], item[0]:item[2]]


                def disc(x, y):
                    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


                base_length_pix = disc((item[0], item[1]), (item[2], item[3]))  # item tọa độ bbox
                pad_crop = 0.038 * base_length_pix
                if item[0] >= pad_crop:
                    xc1 = item[0] - pad_crop
                else:
                    xc1 = item[0]
                if item[1] >= pad_crop:
                    yc1 = item[1] - pad_crop
                else:
                    yc1 = item[1]
                if item[2] + pad_crop <= img.shape[:2][1]:
                    xc2 = item[2] + pad_crop
                else:
                    xc2 = item[2]
                if item[3] + pad_crop <= img.shape[:2][0]:
                    yc2 = item[3] + pad_crop
                else:
                    yc2 = item[3]

                img_crop = img[int(yc1):int(yc2), int(xc1):int(xc2)]  # img là ảnh gốc
                index_count += 1
                cv2.imwrite('F:/SIZING/imgcropped/2022-07-24/' + str(index_count) + '.jpeg', img_crop)

        
            except:
                print("Error")
                pass

        from collections import Counter

        type_dict = Counter(type_arr)

        print(type_dict)
        print(type_dict['Lying down;Straight'])
        print(type_dict['Side lying;Less curved'])
        print(type_dict['Side lying;More curved'])
        print(type_dict['Missing joints'])
        blue_count += type_dict['Missing joints']
        # print("tổng số con xanh dương: ", blue_count)
        white_count += type_dict['Side lying;More curved']
        # print("tổng số con trắng:", white_count)
        sum += total
        # print("tổng:", sum)
        try:
            ti_le_do = ((type_dict['Side lying;More curved'] + type_dict['Missing joints']) / total) * 100
            ti_le_missing_joints = ((type_dict['Missing joints']) / total) * 100
            print('so_con_missing_joint:', type_dict['Missing joints'])
            print('ti_le_do:', ti_le_do)
            print('ti_le_missing_joints:' , ti_le_missing_joints)
        except:
            print("error")
            pass

cv2.destroyAllWindows()
a= blue_count
b= white_count
c= sum
print('blue_count:', a)
print('white_count:', b)
print('sum:', c)
if c != 0:
    count_missing_joints_percentage = (a/c)*100
    count_white_percentage = (b/c)*100
    print('count_missing_joints_percentage:', count_missing_joints_percentage)
    print('count_white_percentage:', count_white_percentage)
else:
    pass

content = ''

folder_path = 'F:/SIZING/2022-07-24/*.json'
list_files = glob.glob(folder_path)

for file in list_files:
    with open(file, 'r') as f:
        a = json.load(f)

    total = len(a)
    type_arr = [item['skeleton_type'] for item in a]
    type_dict = Counter(type_arr)
    if total != 0:
        ti_le_do = ((type_dict['Side lying;More curved'] + type_dict['Missing joints']) / total) * 100
        ti_le_missing_joints = ((type_dict['Missing joints']) / total) * 100
        content += str(file) + '\n'
        content += str(type_dict['Missing joints']) + '\n'
        content += str(ti_le_do) + '\n'
        content += str(ti_le_missing_joints) + '\n'
fo = open("F:/SIZING/ratio/2022-07-24", "w")
fo.write(content)
