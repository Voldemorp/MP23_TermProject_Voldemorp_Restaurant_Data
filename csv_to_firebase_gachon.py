import csv
import os
from google.cloud import firestore

# 서비스 계정 키(JSON 파일)의 경로
service_key_path = 'mp23-termproject-firebase-adminsdk-mpuob-b17820a8cc.json'

# 인증 및 Firestore 초기화
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_key_path
db = firestore.Client()

# 복정 지역 데이터 추가
csv_file_path = 'concat_restaurant/bokjeong_restaurant.csv'  # CSV 파일 경로
collection_name = 'bokjeong_restaurant'  # Firestore 컬렉션 이름

# CSV 파일 읽기 및 Firestore에 데이터 추가
with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_data = csv.reader(file)
    headers = next(csv_data)  # 첫 번째 행을 열 이름으로 사용

    # 첫 번째 행을 건너뛰고 다음 행부터 데이터 추가
    skip_first_row = True

    for row in csv_data:
        if skip_first_row:
            skip_first_row = False
            continue

        data = dict(zip(headers, row))
        data_name = data['사업장명']

        # Firestore 컬렉션의 새 문서 생성 및 데이터 추가
        doc_ref = db.collection(collection_name).document(data_name)
        print(data)
        doc_ref.set(data)

# # 태평 지역 데이터 추가
# csv_file_path = 'concat_restaurant/taepyeong_restaurant.csv'  # CSV 파일 경로
# collection_name = 'taepyeong_restaurant'  # Firestore 컬렉션 이름
#
# # CSV 파일 읽기 및 Firestore에 데이터 추가
# with open(csv_file_path, 'r', encoding='utf-8') as file:
#     csv_data = csv.reader(file)
#     headers = next(csv_data)  # 첫 번째 행을 열 이름으로 사용
#
#     # 첫 번째 행을 건너뛰고 다음 행부터 데이터 추가
#     skip_first_row = True
#
#     for row in csv_data:
#         if skip_first_row:
#             skip_first_row = False
#             continue
#
#         data = dict(zip(headers, row))
#         data_name = data['사업장명']
#
#         # Firestore 컬렉션의 새 문서 생성 및 데이터 추가
#         doc_ref = db.collection(collection_name).document(data_name)
#         print(data)
#         doc_ref.set(data)