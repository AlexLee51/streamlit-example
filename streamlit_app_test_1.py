import datetime as dt
import streamlit as st
import requests
import json
import math
from PIL import Image



kmb_route_json = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/route/')

kmb_route_raw = json.loads(kmb_route_json.content)
kmb_route = kmb_route_raw['data']

kmb_route_total_number = len(kmb_route)

kmb_route_label = []
for i in range(kmb_route_total_number):
    kmb_route_label.append(str(kmb_route[i]['route'] + " (往: " +kmb_route[i]['dest_tc'] + ")"))

kmb_icon = Image.open('KMB_logo.png')
st.image(kmb_icon, caption='KMB')

st.title('香港九龍巴士預計到站時間')

option_route = st.selectbox( '巴士路線:', kmb_route_label )
st.write('已選路線:  ', option_route)

selected_route_index_no = kmb_route_label.index(option_route)

#st.write(kmb_route[selected_route_index_no])


selected_route_no = kmb_route[selected_route_index_no]["route"]
if  kmb_route[selected_route_index_no]["bound"] == "I":
    selected_route_direction = "inbound"
elif kmb_route[selected_route_index_no]["bound"] == "O":
    selected_route_direction = "outbound"

selected_route_service_type = kmb_route[selected_route_index_no]["service_type"]



#Bus route stop list
kmb_route_stop_json = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/route-stop/'+selected_route_no+'/'+selected_route_direction+'/'+selected_route_service_type)
kmb_route_stop_raw = json.loads(kmb_route_stop_json.content)
kmb_route_stop = kmb_route_stop_raw['data']


kmb_route_stop_total_number = len(kmb_route_stop)

kmb_route_stop_id = []
for i in range(kmb_route_stop_total_number):
    kmb_route_stop_id.append(str(kmb_route_stop[i]['stop'] ))


kmb_route_stop_label = []
for i in range(kmb_route_stop_total_number):
    kmb_route_stop_name_json = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/stop/'+kmb_route_stop_id[i])
    kmb_route_stop_name_raw = json.loads(kmb_route_stop_name_json.content)
    kmb_route_stop_name = kmb_route_stop_name_raw['data']
    kmb_route_stop_label.append(str(kmb_route_stop_name["name_tc"]))


option_stop = st.selectbox( '巴士站:', kmb_route_stop_label )
st.write('已選巴士站:  ', option_stop)

selected_stop_index_no = kmb_route_stop_label.index(option_stop)



#Bus route stop eta
if st.button('提交'):
   now = dt.datetime.now()
   kmb_route_stop_eta_json = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/eta/'+ kmb_route_stop_id[selected_stop_index_no] +'/'+ selected_route_no + '/'+ selected_route_service_type )
   kmb_route_stop_eta_raw = json.loads(kmb_route_stop_eta_json.content)
   kmb_route_stop_eta = kmb_route_stop_eta_raw['data']
   kmb_route_stop_eta_total_number = len(kmb_route_stop_eta)
   kmb_route_stop_eta_list = []


   for i in range(kmb_route_stop_eta_total_number):
        kmb_route_stop_eta_list.append(str(kmb_route_stop_eta[i]['eta'] ))

   for i in range(kmb_route_stop_eta_total_number):
       result_index = kmb_route_stop_eta_list[i].find('T')
       temp = kmb_route_stop_eta_list[i]

       hh = int(temp[(result_index + 1):(result_index + 3) ])
       mm = int(temp[(result_index + 4):(result_index + 6) ])
       ss = int(temp[(result_index + 7):(result_index + 9) ])

       now = str(now)
       hh_1 = int(now[11:13])
       mm_1 = int(now[14:16])
       ss_1 = int(now[17:19])
       hh_1 = hh_1+8
       #st.write(str(hh)+str(mm)+str(ss))

       eta_remain_time_in_minutes = math.floor(((hh*3600 + mm * 60 + ss) - (hh_1*3600 + mm_1 * 60 + ss_1))/60)
       #st.write(hh)
       #st.write(mm)
       #st.write(ss)
       #st.write((hh*3600 + mm * 60 + ss))
       #st.write((hh_1*3600 + mm_1 * 60 + ss_1))

       if eta_remain_time_in_minutes <= 0:
           st.write(eta_remain_time_in_minutes)
           eta_remain_time_in_minutes = "--"
       st.subheader("第"+ str(i+1) +"班車")
       st.write("預計"+ str(eta_remain_time_in_minutes)+ "分鐘後到站")
       st.write( " 預計到站時間:" + temp[(result_index + 1):(result_index + 9)])
       st.write(" " )
       st.write(" ")





   #st.write(kmb_route_stop_eta_list)





   st.write(f"現在時間是 {now}")
