import sys
import json

image_caption_dict = {}
a_json = json.load(open('/users/k21026756/anaconda3/envs/a100/lunwen-update-inconsistency-hmcan/dual-inconsistency-rumor-detection-network-master/OFA/OFA-main/results/caption/test_predict.json','r'))
for line in a_json: 
    image_id = line['image_id']
    caption = line['caption']
    image_caption_dict.setdefault(image_id,caption)
    
print (image_caption_dict)
