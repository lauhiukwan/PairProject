from __init__ import *
from models import *
import json
ICCV_number1=Paper.query.filter(Paper.date.like('2013%'),Paper.meeting=='ICCV').count()
ICCV_number2=Paper.query.filter(Paper.date.like('2014%'),Paper.meeting=='ICCV').count()
ICCV_number3=Paper.query.filter(Paper.date.like('2015%'),Paper.meeting=='ICCV').count()
ICCV_number4=Paper.query.filter(Paper.date.like('2016%'),Paper.meeting=='ICCV').count()
ICCV_number5=Paper.query.filter(Paper.date.like('2017%'),Paper.meeting=='ICCV').count()
ICCV_number6=Paper.query.filter(Paper.date.like('2018%'),Paper.meeting=='ICCV').count()
ICCV_number7=Paper.query.filter(Paper.date.like('2019%'),Paper.meeting=='ICCV').count()
ICCV_number8=Paper.query.filter(Paper.date.like('2020%'),Paper.meeting=='ICCV').count()
ICCV_list=[ICCV_number1,ICCV_number2,ICCV_number3,ICCV_number4,ICCV_number5,ICCV_number6,ICCV_number7,ICCV_number8]

ECCV_number1=Paper.query.filter(Paper.date.like('2013%'),Paper.meeting=='ECCV').count()
ECCV_number2=Paper.query.filter(Paper.date.like('2014%'),Paper.meeting=='ECCV').count()
ECCV_number3=Paper.query.filter(Paper.date.like('2015%'),Paper.meeting=='ECCV').count()
ECCV_number4=Paper.query.filter(Paper.date.like('2016%'),Paper.meeting=='ECCV').count()
ECCV_number5=Paper.query.filter(Paper.date.like('2017%'),Paper.meeting=='ECCV').count()
ECCV_number6=Paper.query.filter(Paper.date.like('2018%'),Paper.meeting=='ECCV').count()
ECCV_number7=Paper.query.filter(Paper.date.like('2019%'),Paper.meeting=='ECCV').count()
ECCV_number8=Paper.query.filter(Paper.date.like('2020%'),Paper.meeting=='ECCV').count()
ECCV_list=[ECCV_number1,ECCV_number2,ECCV_number3,ECCV_number4,ECCV_number5,ECCV_number6,ECCV_number7,ECCV_number8]

CVPR_number1=Paper.query.filter(Paper.date.like('2013%'),Paper.meeting=='CVPR').count()
CVPR_number2=Paper.query.filter(Paper.date.like('2014%'),Paper.meeting=='CVPR').count()
CVPR_number3=Paper.query.filter(Paper.date.like('2015%'),Paper.meeting=='CVPR').count()
CVPR_number4=Paper.query.filter(Paper.date.like('2016%'),Paper.meeting=='CVPR').count()
CVPR_number5=Paper.query.filter(Paper.date.like('2017%'),Paper.meeting=='CVPR').count()
CVPR_number6=Paper.query.filter(Paper.date.like('2018%'),Paper.meeting=='CVPR').count()
CVPR_number7=Paper.query.filter(Paper.date.like('2019%'),Paper.meeting=='CVPR').count()
CVPR_number8=Paper.query.filter(Paper.date.like('2020%'),Paper.meeting=='CVPR').count()
CVPR_list=[CVPR_number1,CVPR_number2,CVPR_number3,CVPR_number4,CVPR_number5,CVPR_number6,CVPR_number7,CVPR_number8]
ICCV_map='{name:\'ICCV\',data:'+str(ICCV_list)+'}'
ECCV_map='{name:\'ECCV\',data:'+str(ECCV_list)+'}'
CVPR_map='{name:\'CVPR\',data:'+str(CVPR_list)+'}'
paper_list=ICCV_map+','+ECCV_map+','+CVPR_map
f=open('chart1.txt','w')
f.truncate()
f.write(paper_list)
f.close()
f1=open('chart1.txt')
data=f1.read()
if __name__ == '__main__':

    print(data)


    # list=Paper.query.filter(Paper.meeting=='PVRP').all()
    # for i in range(0,len(list)-1):
    #     list[i].meeting='CVPR'
    # db.session.commit()