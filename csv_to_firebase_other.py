import csv
import os
from google.cloud import firestore

# 서비스 계정 키(JSON 파일)의 경로
service_key_path = 'mp23-termproject-firebase-adminsdk-mpuob-b17820a8cc.json'

# 인증 및 Firestore 초기화
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_key_path
db = firestore.Client()

# 서울 지역 데이터 추가
csv_file_path = 'concat_restaurant/seoul_restaurant.csv'  # CSV 파일 경로
collection_name = 'seoul_restaurant'  # Firestore 컬렉션 이름

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

# 충청 지역 데이터 추가
csv_file_path = 'concat_restaurant/chungcheong_restaurant.csv'  # CSV 파일 경로
collection_name = 'chungcheong_restaurant'  # Firestore 컬렉션 이름

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

# 강원 지역 데이터 추가
csv_file_path = 'concat_restaurant/gangwon_restaurant.csv'  # CSV 파일 경로
collection_name = 'gangwon_restaurant'  # Firestore 컬렉션 이름

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

# 경기 지역 데이터 추가
csv_file_path = 'concat_restaurant/gyeonggi_restaurant.csv'  # CSV 파일 경로
collection_name = 'gyeonggi_restaurant'  # Firestore 컬렉션 이름

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

# 경상 지역 데이터 추가
csv_file_path = 'concat_restaurant/gyeongsang_restaurant.csv'  # CSV 파일 경로
collection_name = 'gyeongsang_restaurant'  # Firestore 컬렉션 이름

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

# 제주 지역 데이터 추가
csv_file_path = 'concat_restaurant/jeju_restaurant.csv'  # CSV 파일 경로
collection_name = 'jeju_restaurant'  # Firestore 컬렉션 이름

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

# 전라 지역 데이터 추가
csv_file_path = 'concat_restaurant/jeolla_restaurant.csv'  # CSV 파일 경로
collection_name = 'jeolla_restaurant'  # Firestore 컬렉션 이름

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

