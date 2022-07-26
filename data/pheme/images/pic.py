import base64
from io import BytesIO
from PIL import Image
import os
import csv

image_text={}
file_path='/users/k21026756/anaconda3/envs/a100/lunwen-update-inconsistency-hmcan/dual-inconsistency-rumor-detection-network-master/data/pheme/pheme_final_fb.csv'
with open(file_path, 'r', encoding='utf-8')as f:
    reader = csv.reader(f)
    for line in reader:
        text_id = line[0].strip('\t').strip('\ufeff').strip('"').strip('\t')
        #tweet = line[1].strip('\t')
        image_id = line[2].strip('\t').strip('\ufeff').strip('"').strip('\t') 
        #label = int(line[3].strip('\t'))
        #mids = line[4].strip('\t')
        #print ('text_id-----------',text_id)
        #print ('image_id----------',image_id)
        image_text.setdefault(image_id,text_id)


pic_path='/users/k21026756/anaconda3/envs/a100/lunwen-update-inconsistency-hmcan/dual-inconsistency-rumor-detection-network-master/data/pheme/images'
files = os.listdir(pic_path)
for p in files:
    if p.split('.')[1] != 'jpg':
        continue
    img = Image.open(p)
    img = img.convert('RGB')  #add by zhou
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    base64_str = str(base64_str, encoding='utf-8')

    image_id=p.split('.')[0]
    uniq_id=image_text[image_id]
    image_id=image_id
    caption='testcaption'
    predicted_object_labels='predicted_object_labels'

    out_str = uniq_id + '\t' + image_id + '\t' + caption +'\t'+ predicted_object_labels +'\t'+ base64_str
    print(out_str)

