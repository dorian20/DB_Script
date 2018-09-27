# -*- coding: utf-8 -*-
import sys
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import blake2b
import os
import json
from pprint import pprint


def encrypt_mytext(mytext,input_key):
    h = blake2b(digest_size=16)
    h.update(input_key.encode())
    key=h.hexdigest()
    #print(key)
    data=str(mytext)+" "
    cipher = AES.new(b64decode(key), AES.MODE_CBC, iv=b'0123456789abcdef')
    padded_data = pad(data.encode("utf-8"), cipher.block_size)
    encrypt_text = cipher.encrypt(padded_data)
    #print(encrypt_text)    
    return b64encode(encrypt_text).decode("utf-8")


def decrypt_mytext(encrypt_text,input_key):
    #print(ciphertext)    
    h = blake2b(digest_size=16)
    h.update(input_key.encode())
    key=h.hexdigest()
    #print(key)
    ciphertext = b64decode(encrypt_text.encode("utf-8"))
    cipher= AES.new(b64decode(key), AES.MODE_CBC, iv=b'0123456789abcdef')
    decrypt_text=str(cipher.decrypt(ciphertext).decode("utf-8")).split(' ')[0]
    return decrypt_text

def read_conn_info(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    encrypt_json=json.loads(line)
    input_enc_key=input("enc key: ")
    server_infos_dec={}
    for key,value1 in encrypt_json.items():
        dec_key=decrypt_mytext(key,input_enc_key)
        server_infos_dec[dec_key]={}
        for key2,value2 in value1.items():
            dec_key2=decrypt_mytext(key2,input_enc_key)
            dec_value2=decrypt_mytext(value2,input_enc_key)
            server_infos_dec[dec_key][dec_key2]=dec_value2
    return server_infos_dec

def encrypt_json_save(server_infos,file_name):
    server_infos_enc={}
    input_enc_key=input("encrypt key:")
    input_enc_key2=input("encrypt key(again):")
    if input_enc_key != input_enc_key2:
        print("다른키입력됨")
        exit(1)

    for key,value1 in server_infos.items():
        #print(key)
        
        enc_key=encrypt_mytext(key,input_enc_key)
        server_infos_enc[enc_key]={}
        for key2,value2 in value1.items():
            enc_key2=encrypt_mytext(key2,input_enc_key)
            enc_value2=encrypt_mytext(value2,input_enc_key)
            server_infos_enc[enc_key][enc_key2]=enc_value2

    for key,value in server_infos_enc.items():
        print(decrypt_mytext(key,input_enc_key))
    #file_name = "conn_info.json"

    with open(file_name, 'w') as outfile:
        json.dump(server_infos_enc, outfile)

def InputNumber(min_number,max_number):
    while True:
        try:
            number = int(input("숫자를 입력하세요: "))
            if(number >=min_number and number <= max_number):
                return number
            
            print(str(min_number)+"~"+str(max_number)+"까지 입력")
        except Exception as ex:
            continue

if __name__=='__main__':
    try:
        file_name = "conn_info.json"
        print("1. 새로생성(conn_info.json 파일이 있으면 덮어써집니다.)")
        print("2. 기존파일출력")
        print("3. 종료")

        menu = InputNumber(1,3)

        if menu == 3:
            sys.exit()
        
        elif menu == 1: 
       
            server_infos = {}

            server_infos['ltcmdev'] = {"source_bastion_ip" : '정보' 
                            , "source_bastion_user" : '정보'  
                            , "source_bastion_pwd" : '정보'  
                            , "source_endpoint" : '정보'  
                            , "source_db_user" : "정보"
                            , "source_db_pwd" : "정보"
                            }
            
            encrypt_json_save(server_infos,file_name)

        elif menu == 2:
            server_infos=read_conn_info(file_name)
            print(str(json.dumps(server_infos,indent=4)))


    except Exception as ex:
        print(ex)
        sys.exit()